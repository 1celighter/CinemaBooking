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

@app.get(
    "/Movies/{movie_id}",
    tags=["Catalog"],
    summary="There you can get a film from our cataloge"
)
def GetMovie(movie_id: int):
    for Movie in Movies:
        if Movie["MID"] == movie_id:
            return {
                "Message": "there ur movie",
                "Movie": Movie
            }
    raise HTTPException(status_code=404, detail=f"Movie with this {movie_id} Id has not found")


class MovieSchema(BaseModel):
    MID: int = Field(ge=0)
    MovieName: str = Field(min_length=4, max_length=40)
    MovieStudio: str = Field(min_length=2, max_length=50)
    StudioEmail: EmailStr
    MetaCriticScore: float = Field(ge=0, le=10)
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
        "Movie Status": AddMovie,
        "Status": True,
        "After word message": "If u did mistake on add film u can delete it or make some adjustments",
    }


@app.put("/UpdateMovie/{Movie_Id}",
         tags=["Edit"],
         summary="Here we can edit our movies name rating and etc..."
)
def UpdateMovie(Movie_Id: int, EditMovie:MovieSchema) -> dict:
    index = Movie_Id - 1 
    Movie_dict = EditMovie.model_dump()
    Movie_dict["Movie_Id"] = Movie_Id
    Movies[index] = Movie_dict
    return {
        "Message": f"Movie with {Movie_Id} has been edited",
        "Edited Movie": Movies[index]
    }

@app.delete("/DeleteMovie/{Movie_Id}",
            tags=["Edit"],
            summary="Delete film if it need it by MID")

def DeleteMovie(Movie_Id: int) -> dict:
    Deleted_Movie = Movies.pop(Movie_Id - 1)
    return {
        "Message": f"Movie with this {Movie_Id} Id has been deleted",
        "Deleted Content": Deleted_Movie
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
