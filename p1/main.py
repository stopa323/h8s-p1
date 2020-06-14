# type: ignore
import uvicorn

from fastapi import FastAPI
from mongoengine import connect, disconnect

from p1.common.config import get_config
from p1.router import craftplan


app = FastAPI()
app.include_router(craftplan.router)


@app.on_event("startup")
async def startup():
    cfg = get_config()
    con = connect(db=cfg.get("db", "db_name"), host=cfg.get("db", "connection"))
    con.server_info()
    print("DB connection OK")


@app.on_event("shutdown")
async def shutdown_event():
    disconnect()
    print("Disconnected from DB")


if __name__ == "__main__":
    cfg = get_config()
    uvicorn.run(app, host=cfg.get("DEFAULT", "bind_host"),
                port=cfg.getint("DEFAULT", "bind_port"))
