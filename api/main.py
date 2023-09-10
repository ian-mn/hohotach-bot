from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from settings import settings

from api.v1 import recommendation, reactions

app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)


app.include_router(
    recommendation.router,
    prefix="/api/v1/recommendation",
    tags=["Recomendation"],
)
app.include_router(
    reactions.router,
    prefix="/api/v1/reactions",
    tags=["Reactions"],
)
