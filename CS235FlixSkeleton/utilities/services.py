from typing import Iterable
import random

from CS235FlixSkeleton.adapters.repository import AbstractRepository
from CS235FlixSkeleton.domainmodel.model import Movie


def get_genre_names(repo: AbstractRepository):
    genres = repo.get_genre()
    genre_names = [genre.genre_name for genre in genres]

    return genre_names



# ============================================
# Functions to convert dicts to model entities
# ============================================

def movie_to_dict(movie: Movie):
    movie_dict = {
        'title': movie.title,
        'release_year': movie.release_year,
        "description": movie.description,
    }
    return movie_dict


def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]
