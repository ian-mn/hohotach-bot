import json
from datetime import datetime

from odnoklassniki_parser.settings import DBSettings
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base
from psycopg2.errors import UniqueViolation

settings = DBSettings()

url = URL.create(
    drivername="postgresql",
    username=settings.user,
    password=settings.password.get_secret_value(),
    host=settings.host,
    port=settings.port,
    database=settings.name,
)

engine = create_engine(url)

Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"

    url = Column(String(), primary_key=True)
    name = Column(String(), nullable=False)


class Meme(Base):
    __tablename__ = "memes"

    hashsum = Column(String(), primary_key=True)
    image_url = Column(String(), nullable=False)
    description = Column(String(), nullable=True)
    likes = Column(Integer(), default=0)
    dislikes = Column(Integer(), default=0)
    group_url = Column(String(), ForeignKey("groups.url"))
    created_on = Column(DateTime(), default=datetime.now())


Base.metadata.create_all(engine)


from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


def get_groups():
    rows = session.query(Group.url).all()
    return [x.url for x in rows]


with open("groups.json", "r", encoding="utf-8") as f:
    groups = json.loads(f.read())

urls = get_groups()
for group in groups:
    if group["url"] not in urls:
        session.add(Group(**group))
session.commit()


def insert(item) -> None:
    with Session() as session:
        try:
            session.add(item)
            session.commit()
        except UniqueViolation:
            pass
