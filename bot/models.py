from pydantic import BaseModel, HttpUrl


class Meme(BaseModel):
    hashsum: str
    image_url: HttpUrl
    description: str | None
