from pydantic import BaseModel, EmailStr, Field, ConfigDict

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