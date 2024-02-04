import fastapi
import uvicorn
from src.server.router import routers
import sys

sys.path.append('C:/museum-use-case')

import settings

app = fastapi.FastAPI(title='Museum', version='Beta 0.1', description='Muesum app bro')

[app.include_router(router) for router in routers]

@app.get(path='/', include_in_schema=False)
def index() -> fastapi.responses.RedirectResponse:
    return fastapi.responses.RedirectResponse('/docs')


def start_server() -> None:
    uvicorn.run(app='server:app', host=settings.HOST, port=settings.PORT)


if settings.DEBUG:
    if __name__ == "__main__":
        start_server()