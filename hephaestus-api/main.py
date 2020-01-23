import uvicorn
from fastapi import FastAPI

from common.config import get_config
from router import blueprint

app = FastAPI()
app.include_router(blueprint.router, prefix="/v1")


if __name__ == "__main__":
    # TODO: hook to on start events
    cfg = get_config()
    uvicorn.run(app, host=cfg.get("DEFAULT", "bind_host"),
                port=cfg.getint("DEFAULT", "bind_port"))
