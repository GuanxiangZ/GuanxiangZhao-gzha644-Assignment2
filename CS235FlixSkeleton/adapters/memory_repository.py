import csv
import os
from datetime import date, datetime
from typing import List

from bisect import bisect, bisect_left, insort_left

from werkzeug.security import generate_password_hash

from CS235FlixSkeleton.adapters.repository import AbstractRepository, RepositoryException
from CS235FlixSkeleton.domainmodel.model import User, Movie, Actor, Director, Genre, Review
from CS235FlixSkeleton.datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from CS235FlixSkeleton.domainmodel.watchlist import WatchList


class MemoryRepository(AbstractRepository):

    def __init__(self):
        self._movies = WatchList()
        self._users = list()
        self._actors = list()
        self._directors = list()
        self._genres = list()
        self._reviews = list()
        self._i = iter(self._movies)

    def add_user(self, user: User):
        self._users.append(user)

    def get_user(self, username) -> User:
        user = None
        for u in self._users:
            if u.user_name == username:
                user = u
        return user

    def add_movie(self, movie: Movie):
        self._movies.add_movie(movie)

    def get_movie(self, index : int) -> Movie:
        return self._movies.select_movie_to_watch(index)

    def get_movie_by_page(self, page: int):
        return self._movies.select_movie_by_page(page)

    def get_page_of_previous_movie(self, movie: Movie):
        pre_page = movie.page - 1
        if pre_page < 0:
            return 0
        else:
            return pre_page

    def get_page_of_next_movie(self, movie: Movie):
        return (movie.page + 1)

    def get_number_of_movies(self):
        return self._movies.size()

    def get_first_movie(self) -> Movie:
        return self._movies.first_movie_in_watchlist()

    def get_last_movie(self) -> Movie:
        return self._movies.last_movie_in_watchlist()

    def get_next_movie(self):
        return next(self._i)

    def add_actor(self, actor: Actor):
        self._actors.append(actor)

    def get_actor(self) -> List[Actor]:
        return self._actors

    def add_director(self, director: Director):
        self._directors.append(director)

    def get_director(self) -> List[Director]:
        return self._directors

    def add_genre(self, genre: Genre):
        self._genres.append(genre)

    def get_genre(self) -> List[Genre]:
        return self._genres


def read_csv_file():
    movie_file_reader = MovieFileCSVReader(os.path.join("E:", os.sep, "cs235", "Assignment", "CS235FlixSkeleton", "datafiles", "Data1000Movies.csv"))
    movie_file_reader.read_csv_file()
    return movie_file_reader

def load_movies(repo: MemoryRepository):
    movie_file_reader = read_csv_file()
    movies_list = movie_file_reader.dataset_of_movies
    for movie in movies_list:
        repo.add_movie(movie)

def load_actors(repo: MemoryRepository):
    movie_file_reader = read_csv_file()
    actors_list = movie_file_reader.dataset_of_actors
    for actor in actors_list:
        repo.add_actor(actor)

def load_directors(repo: MemoryRepository):
    movie_file_reader = read_csv_file()
    directors_list = movie_file_reader.dataset_of_directors
    for director in directors_list:
        repo.add_director(director)

def load_genres(repo: MemoryRepository):
    movie_file_reader = read_csv_file()
    genres_list = movie_file_reader.dataset_of_genres
    for genre in genres_list:
        repo.add_genre(genre)

def populate(repo: MemoryRepository):
    # Load articles and tags into the repository.
    load_movies(repo)
    load_actors(repo)
    load_directors(repo)
    load_genres(repo)
