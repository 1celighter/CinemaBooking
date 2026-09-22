import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, EmailStr, Field

app = FastAPI()

Movies = []


@app.get(
    "/MoviesCatalog",
    tags=["Catalog"],
    summary="There is our Catalog where we can pull back our Movies in our Cinema",
)
def MoviesCatalog() -> dict:
    return {
        "Message": "There all our catalog of movies in this cinema!",
        "Movies": Movies,
    }


class MovieSchema(BaseModel):
    MID: int = Field(ge=0)
    MovieName: str = Field(ge=4, le=40)
    MovieStudio: str = Field(ge=2, le=50)
    MovieRating: int = Field(ge=0, le=10)
    UserScore: int = Field(ge=0, le=100)
    ContentRating: int = Field(ge=0, le=18)
    MovieGenre: str = Field(ge=0, le=180)


@app.post(
    "/AddMovie",
    tags=["Catalog"],
    summary="If you need add a Movie to our catalog add this here with this endpoint",
)
def AddMovie():
    pass


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
