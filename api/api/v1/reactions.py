from http import HTTPStatus

from db import DBExctractor, get_base_service
from fastapi import APIRouter, Depends, HTTPException
from models import ReactionType
from pydantic import HttpUrl

router = APIRouter()


@router.post(
    "/like",
    summary="Like added",
)
async def add_like(
    user_id: str,
    image_url: HttpUrl,
    service: DBExctractor = Depends(get_base_service),
) -> None:
    reaction = ReactionType.LIKE
    service.add_reaction(user_id, image_url, reaction)


@router.post(
    "/dislike",
    summary="Dislike added",
)
async def add_dislike(
    user_id: str, image_url: HttpUrl, service: DBExctractor = Depends(get_base_service)
) -> None:
    reaction = ReactionType.DISLIKE
    service.add_reaction(user_id, image_url, reaction)
