from pydantic import BaseModel
from typing import Optional

class MovieBase(BaseModel):
    title : Optional[str] = None
    year : Optional[int] = None

class MovieCreate(MovieBase):
    title: str
    year: int

class Movie(MovieBase):
    title : str
    year : int
    