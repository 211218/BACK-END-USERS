from fastapi import FastAPI
from config.api import tags_metadata
from routers.teacher import teacher
from routers.admin import admin
import uvicorn

app = FastAPI(
    title="INTEGRADOR",
    description="REST API OFFICIAL",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(teacher)
app.include_router(admin)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
