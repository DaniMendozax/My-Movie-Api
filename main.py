from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.logins import login_users

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(login_users)
app.include_router(movie_router)


Base.metadata.create_all(bind=engine)


# movies = [
#     {
#         'id': 1,
#         'title': 'Avatar',
#         'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
#         'year': '2009',
#         'rating': 7.8,
#         'category': 'Acción'
#     },
#     {
#         'id': 2,
#         'title': 'Avatar 2',
#         'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
#         'year': '2009',
#         'rating': 7.8,
#         'category': 'Acción'
#     }
# ]



