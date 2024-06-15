from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from core.orm import initializeTables
from routes import apis, webs

app = FastAPI()

app.mount('/statics', StaticFiles(directory='statics'), name='statics')
app.include_router(apis.router)
app.include_router(webs.router)

@app.on_event('startup')
def on_startup():
    # recomend implement alembic migration instead of this
    initializeTables()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)