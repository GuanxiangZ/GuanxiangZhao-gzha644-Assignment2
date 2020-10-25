from datetime import date, datetime
from typing import List
import os

import pytest

from CS235FlixSkeleton.domainmodel.model import User, Movie, Actor, Director, Genre, Review
from CS235FlixSkeleton.adapters import memory_repository
from CS235FlixSkeleton.adapters.memory_repository import MemoryRepository
from CS235FlixSkeleton.adapters.repository import RepositoryException



@pytest.fixture
def in_memory_repo():
    repo = MemoryRepository()
    memory_repository.populate(repo)
    return repo


def test_repository_can_add_a_user(in_memory_repo):
    user = User('dave', '123456789')
    in_memory_repo.add_user(user)

    assert in_memory_repo.get_user('dave') is user


def test_repository_can_retrieve_movie_count(in_memory_repo):
    number_of_movies = in_memory_repo.get_number_of_movies()

    # Check that the query returned 1000 Articles.
    assert number_of_movies == 1000


def test_repository_can_add_movie(in_memory_repo):
    movie = Movie("Moana", 2000)
    in_memory_repo.add_movie(movie)

    assert movie.id == 1000

def test_repository_can_get_next_movie(in_memory_repo):
    m1 = in_memory_repo.get_first_movie()
    assert in_memory_repo.get_next_movie() is m1


def test_repository_can_get_actors(in_memory_repo):
    actors : List[Actor] = in_memory_repo.get_actor()
    assert len(actors) == 1985


def test_repository_can_get_directors(in_memory_repo):
    actors : List[Director] = in_memory_repo.get_director()
    assert len(actors) == 644


def test_repository_can_get_genres(in_memory_repo):
    actors : List[Genre] = in_memory_repo.get_genre()
    assert len(actors) == 20

def test_repository_can_get_movie_by_page(in_memory_repo):
    movies : List[Movie] = in_memory_repo.get_movie_by_page(99)
    assert len(movies) == 10
    movie = Movie("Moana", 2000)
    in_memory_repo.add_movie(movie)
    movies: List[Movie] = in_memory_repo.get_movie_by_page(100)
    assert len(movies) == 1

def test_get_page(in_memory_repo):
    last_movie = in_memory_repo.get_last_movie()
    assert in_memory_repo.get_page_of_previous_movie(last_movie) == 99
    movie = Movie("Moana", 2000)
    movie2 = Movie("aaaa", 1999)
    in_memory_repo.add_movie(movie)
    in_memory_repo.add_movie(movie2)
    assert in_memory_repo.get_page_of_next_movie(last_movie) == 100
