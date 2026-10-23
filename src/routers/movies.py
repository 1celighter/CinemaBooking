from fastapi import APIRouter, HTTPException
from src.schemas import MovieSchema

router = APIRouter(prefix="/Movies", tags=["Catalog"])

Movies = []

@router.get("",
            summary="There is our Catalog where we can pull back our Movies in our Cinema")
def get_catalog() -> dict:
    return {
        "Message": "There all our catalog of movies in this cinema!",
        "Movies": Movies
    }

@router.get("/{Movie_Id}",
            summary="There you can get a film from our cataloge"
            )
def GetMovie(Movie_Id: int):
    for Movie in Movies:
        if Movie["MID"] == Movie_Id:
            return {
                "Message": "There your movie",
                "Movie": Movie
            }
    
    raise HTTPException(status_code=404, detail=f"Movie with this {Movie_Id} id has not found")


@router.post("/Add",
             summary="If you need add a Movie to our cataloge add this here with this endpoint",
             status_code=201
             )
def AddMovie(AddMovie:MovieSchema) -> dict:
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
        "After word message": "If u did mistake on add film u can delete it or make some adjustments"
    }

@router.put("/Update/{Movie_Id}",
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
        "Updated Movie": Movies[index]
    }

@router.delete("/Delete/{Movie_Id}",
               tags=["Edit"],
               summary="Delete film if it need it by MID")
def DeleteMovie(Movie_Id: int) -> dict:
    Deleted_Movie = Movies.pop(Movie_Id - 1)
    return { 
        "Message": f"Movie with this {Movie_Id} id has been deleted",
        "Deleted content": Deleted_Movie
    }
