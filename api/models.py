from pydantic import BaseModel, HttpUrl


class MemeOut(BaseModel):
    image_url: HttpUrl
    description: str | None
