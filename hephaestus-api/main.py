import uvicorn
from fastapi import FastAPI

from common.config import get_config
from router import blueprint, node_mold

app = FastAPI()
app.include_router(blueprint.router, prefix="/v1")
app.include_router(node_mold.router, prefix="/v1/molds")


if __name__ == "__main__":
    # TODO: hook to on start events
    cfg = get_config()
    uvicorn.run(app, host=cfg.get("DEFAULT", "bind_host"),
                port=cfg.getint("DEFAULT", "bind_port"))
