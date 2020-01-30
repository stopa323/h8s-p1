import uvicorn
from fastapi import FastAPI

from common.config import get_config
from common.db import load_core_schemata
from router import blueprint, schemata

app = FastAPI()
app.include_router(blueprint.router, prefix="/v1")
app.include_router(schemata.router, prefix="/v1")


@app.on_event("startup")
async def startup_event():
    load_core_schemata()


if __name__ == "__main__":
    cfg = get_config()
    uvicorn.run(app, host=cfg.get("DEFAULT", "bind_host"),
                port=cfg.getint("DEFAULT", "bind_port"))
