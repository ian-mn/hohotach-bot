from http import HTTPStatus

from db import DBExctractor, get_base_service
from fastapi import APIRouter, Depends, HTTPException
from models import MemeOut

router = APIRouter()


@router.get(
    "/",
    response_model=MemeOut,
    summary="Meme recommendation for user",
    response_description="Image URL and description",
)
async def get_recommendation(
    user_id: str,
    service: DBExctractor = Depends(get_base_service),
) -> MemeOut:
    meme = service.get_random()
    if not meme:
        raise HTTPException(HTTPStatus.NOT_FOUND, detail="Meme not found.")
    return MemeOut(**meme)
