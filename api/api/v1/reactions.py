from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from pydantic import HttpUrl

router = APIRouter()


@router.post(
    "/like",
    summary="Like added",
)
async def add_like(user_id: str, image_url: HttpUrl) -> None:
    raise HTTPException(status_code=HTTPStatus.IM_A_TEAPOT)
    return


@router.post(
    "/dislike",
    summary="Dislike added",
)
async def add_dislike(user_id: str, image_url: HttpUrl) -> None:
    raise HTTPException(status_code=HTTPStatus.IM_A_TEAPOT)
    return
