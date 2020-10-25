from datetime import date

import pytest

from CS235FlixSkeleton.adapters import memory_repository
from CS235FlixSkeleton.adapters.memory_repository import MemoryRepository
from CS235FlixSkeleton.news import services as news_services
from CS235FlixSkeleton.news.services import NonExistentArticleException


@pytest.fixture
def in_memory_repo():
    repo = MemoryRepository()
    memory_repository.populate(repo)
    return repo


def test_can_get_movie(in_memory_repo):
    movie_index = 2

    movie_as_dict = news_services.get_movie(movie_index, in_memory_repo)

    assert movie_as_dict['title'] == 'Split'
    assert movie_as_dict['release_year'] == 2016
    genre_name = [dictionary['name'] for dictionary in movie_as_dict['genres']]
    assert 'Horror' in genre_name
    actor_name = [dictionary['name'] for dictionary in movie_as_dict['actors']]
    assert 'James McAvoy' in actor_name
    assert 'Anya Taylor-Joy' in actor_name


def test_cannot_get_movie_with_non_existent_id(in_memory_repo):
    movie_index = 1002

    # Call the service layer to attempt to retrieve the Article.
    with pytest.raises(news_services.NonExistentArticleException):
        news_services.get_movie(movie_index, in_memory_repo)


def test_get_first_movie(in_memory_repo):
    movie_as_dict = news_services.get_first_movie(in_memory_repo)

    assert movie_as_dict['title'] == "Guardians of the Galaxy"


def test_get_last_movie(in_memory_repo):
    movie_as_dict = news_services.get_last_movie(in_memory_repo)

    assert movie_as_dict['title'] == 'Nine Lives'