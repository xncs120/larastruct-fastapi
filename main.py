from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from core.database import engine
from sqlmodel import SQLModel
from models import user_model # need to add all models here to create table if no exists
from routes import apis, webs

app = FastAPI()

app.mount("/statics", StaticFiles(directory="statics"), name="statics")
app.include_router(apis.router)
app.include_router(webs.router)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)