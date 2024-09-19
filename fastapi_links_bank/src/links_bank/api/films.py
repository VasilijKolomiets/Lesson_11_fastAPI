"""Модуль для обробки всіх HTTP-roots для '/films' - тобто фільмів."""
from fastapi import APIRouter
from fastapi import Depends

from ..models.films import Film, FilmCategory
from ..services.films import FilmsService


router = APIRouter(prefix="/films")

# not hardcoded `film_category` param magically will be searching in query string
@router.get("/", response_model=list[Film])
def read_films(film_category: FilmCategory | None = None, service: FilmsService = Depends()):
    return service.get_all(film_category)
