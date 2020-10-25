from typing import List, Iterable

from CS235FlixSkeleton.adapters.repository import AbstractRepository
from CS235FlixSkeleton.domainmodel.model import User, Movie, Actor, Director, Genre, Review,make_review


class NonExistentArticleException(Exception):
    pass


class UnknownUserException(Exception):
    pass


def get_movie(id: int, repo: AbstractRepository):
    movie = repo.get_movie(id)

    if movie is None:
        raise NonExistentArticleException

    return movie_to_dict(movie)


def get_movies_by_page(page, repo: AbstractRepository):
    # Returns articles for the target date (empty if no matches), the date of the previous article (might be null), the date of the next article (might be null)

    movies = repo.get_movie_by_page(page)

    movies_dto = list()
    prev_page = next_page = None

    if len(movies) > 0:
        prev_page = repo.get_page_of_previous_movie(movies[0])
        next_page = repo.get_page_of_next_movie(movies[0])

        # Convert Articles to dictionary form.
        movies_dto = movies_to_dict(movies)

    return movies_dto, prev_page, next_page


def get_first_movie(repo: AbstractRepository):

    movie = repo.get_first_movie()

    return movie_to_dict(movie)


def get_last_movie(repo: AbstractRepository):

    movie = repo.get_last_movie()
    return movie_to_dict(movie)


# ============================================
# Functions to convert model entities to dicts
# ============================================

def movie_to_dict(movie: Movie):
    movie_dic = {
        'title': movie.title,
        'release_year': movie.release_year,
        'actors': actors_to_string(movie.actors),
        'genres': genres_to_string(movie.genres),
        'director': movie.director.director_full_name,
        'runtime_minutes': movie.runtime_minutes,
        "description": movie.description,
        'id': movie.id,
        'page': movie.page
    }
    return movie_dic


def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]


def actors_to_string(actors: Iterable[Actor]):
    s = ""
    for actor in actors:
        s = s + actor.actor_full_name + " "
    return s




def genres_to_string(genres: Iterable[Genre]):
    s = ""
    for genre in genres:
        s = s + genre.genre_name + " "
    return s


# ============================================
# Functions to convert dicts to model entities
# ============================================

def dict_to_movie(dict):
    movie = Movie(dict.title, dict.release_year)
    # Note there's no comments or tags.
    return movie
