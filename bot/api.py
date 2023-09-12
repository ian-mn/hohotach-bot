import requests
from models import Meme


def get_recommended(user_id: str):
    with requests.get(
        "http://api:8010/api/v1/recommendation",
        params={"user_id": user_id},
    ) as r:
        return Meme(**r.json())


def add_reaction(user_id: str):
    with requests.get(
        "http://api:8010/api/v1/recommendation",
        params={"user_id": user_id},
    ) as r:
        return Meme(**r.json())
