import uvicorn
from fastapi import FastAPI
from src.routers.movies import router as movies_router

app = FastAPI()

app.include_router(movies_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
