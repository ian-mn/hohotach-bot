from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from models import MemeOut

router = APIRouter()


@router.get(
    "/",
    response_model=MemeOut,
    summary="Meme recommendation for user",
    response_description="Image URL and description",
)
async def get_recommendation(user_id: str) -> MemeOut:
    raise HTTPException(status_code=HTTPStatus.IM_A_TEAPOT)
    return
