from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieServices
from schemas.movie import Movie

movie_router = APIRouter()



@movie_router.get('/movies', tags=['movies get'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieServices(db).get_movies()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_router.get('/movies/{id}', tags=['movies get'], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    db = Session()
    result = MovieServices(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No encontrado"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_router.get('/movies/', tags=['movies get'],  response_model=Movie)
def get_movies_by_category(category: str = Query(min_length=2, max_length=15)) -> Movie:
    # data = [movie for movie in movies if movie['category'] == category]
    db = Session()
    result = MovieServices(db).get_movies_by_category(category)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No encontrado"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieServices(db).create_movie(movie)
    return JSONResponse(content={"message": "Se ha registrado correctamente"}, status_code=201)


@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    result = MovieServices(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No encontrado"})
    MovieServices(db).update_movie(id, movie)
    return JSONResponse(content={"message": "Se ha actualizado correctamente"}, status_code=200)

    # for item in movies:
    #     if item["id"] == id:
    #         item.update(movie)
    # return JSONResponse(content= {"message": "Se ha actualizado correctamente"}, status_code=200)


@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    db = Session()
    result = MovieServices(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Movie not found'})
    MovieServices(db).delete_movie(id)
    return JSONResponse(content={"message": "Se ha elimindado correctamente"}, status_code=200)
    # for item in movies:
    #     if item["id"] == id:
    #         movies.remove(item)
    # return JSONResponse(content={"message": "Se ha elimindado correctamente"}, status_code=200)
