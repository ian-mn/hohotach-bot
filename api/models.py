from enum import Enum

from pydantic import BaseModel, HttpUrl


class MemeOut(BaseModel):
    hashsum: str
    image_url: HttpUrl
    description: str | None


class ReactionType(Enum):
    LIKE = "likes"
    DISLIKE = "dislikes"
