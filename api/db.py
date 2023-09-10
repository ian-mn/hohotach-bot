from contextlib import contextmanager
from functools import lru_cache

import psycopg2
from models import ReactionType
from psycopg2.extras import DictCursor
from pydantic import HttpUrl
from settings import DBSettings, Settings


class DBExctractor:
    def __init__(self) -> None:
        self.db_settings = DBSettings()
        self.settings = Settings()

    @contextmanager
    def __conn_context(self):
        """PostgreSQL connection context manager."""
        conn = psycopg2.connect(**self.settings.dict(), cursor_factory=DictCursor)
        psycopg2.extras.register_uuid()
        yield conn
        conn.close()

    def add_reaction(
        self, user_id: str, image_url: HttpUrl, reaction: ReactionType
    ) -> None:
        with self.__conn_context() as conn:
            curs = conn.cursor()
            curs.execute(
                f"""
                update memes
                set {reaction.value} = {reaction.value} + 1
                where image_url = '{image_url}';
                """
            )
            conn.commit()

    def get_random(self):
        with self.__conn_context() as conn:
            curs = conn.cursor()
            curs.execute(
                f"""
                select
                    image_url,
                    description
                from memes
                where
                    case when likes + dislikes = 0 then 0
                    else dislikes / (likes + dislikes + 1)
                    end < {self.settings.DISLIKE_SHARE_THRESHOLD}
                order by random()
                limit 1;
                """
            )
            return curs.fetchone()


@lru_cache()
def get_base_service() -> DBExctractor:
    return DBExctractor()
