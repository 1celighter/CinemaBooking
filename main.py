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
    MovieName: str = Field(min_length=4, max_length=40)
    MovieStudio: str = Field(min_length=2, max_length=50)
    StudioEmail: EmailStr
    MetaCriticScore: int = Field(ge=0, le=10)
    UserScore: int = Field(ge=0, le=100)
    ContentRating: int = Field(ge=0, le=18)
    MovieGenre: str = Field(min_length=0, max_length=180)

    model_config = ConfigDict(extra="forbid")


@app.post(
    "/AddMovie",
    tags=["Catalog"],
    summary="If you need add a Movie to our catalog add this here with this endpoint",
    status_code=201,
)
def AddMovie(AddMovie: MovieSchema) -> dict:
    Movies.append(
        {
            "MID": len(Movies) + 1,
            "Movie Name": AddMovie.MovieName,
            "Movie Studio": AddMovie.MovieStudio,
            "Studio's Email": AddMovie.StudioEmail,
            "Movie Rating": AddMovie.MetaCriticScore,
            "User Score": AddMovie.UserScore,
            "Content Rating": AddMovie.ContentRating,
            "Movie Genre": AddMovie.MovieGenre,
        }
    )
    return {
        "Message": "New movie has been added to our system",
        "Movie Stats": AddMovie,
        "Status": True,
        "After word message": "If u did mistake on add film u can delete it or make some adjustments",
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
