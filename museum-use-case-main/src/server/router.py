from src.server.service import RouterManager
from src.server.database import pydantic_models, database_models

routers = (
    RouterManager(database_model=database_models.Artists, pydantic_model=pydantic_models.ArtistModel, prefix='/artists', tags=['Artists']).fastapi_router,
)