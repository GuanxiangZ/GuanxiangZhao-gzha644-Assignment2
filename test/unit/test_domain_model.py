from datetime import date

from CS235FlixSkeleton.domainmodel.model import User, Movie, Actor, Director, Genre, Review, make_review
from CS235FlixSkeleton.domainmodel.watchlist import WatchList

import pytest


@pytest.fixture()
def movie():
    movie = Movie("Moana", 2016)
    return movie

@pytest.fixture()
def user():
    return User('Martin', 'pw12345')

@pytest.fixture()
def director():
    return Director("Ron Clements")

@pytest.fixture()
def actors():
    return [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]

@pytest.fixture()
def genre():
    return Genre("Horror")


def test_user_construction(user):
    assert user.user_name == 'martin'
    assert user.password == 'pw12345'
    assert repr(user) == '<User martin>'

    for review in user.reviews:
        # User should have an empty list of Comments after construction.
        assert False


def test_movie_construction(movie, director, actors, genre):
    movie.director = director
    for actor in actors:
        movie.add_actor(actor)
    movie.runtime_minutes = 107
    movie.add_genre(genre)
    assert movie.title == "Moana"
    assert movie.release_year == 2016
    assert movie.director == director
    assert movie.actors == actors
    assert genre in movie.genres
    assert movie in genre.movie_list
    assert movie in actors[0].movie_list
    assert movie in director.movie_list


def test_article_less_than_operator():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana", 2015)
    movie3 = Movie("Moane", 2016)
    assert movie2 < movie1
    assert movie1 < movie3
    assert movie2 < movie3


def test_make_review_establishes_relationships(movie, user):
    review_text = "This movie was very enjoyable."
    rating = 8
    review = Review(movie, review_text, rating)
    user.add_review(review)

    assert review in user.reviews
    assert user is review.user
    assert review in movie.get_review()
    assert review.movie is movie

def test_watchlist():
    watchlist = WatchList()
    assert watchlist.size() == 0
    m1 = Movie("Moana", 2016)
    m2 = Movie("Ice Age", 2002)
    m3 = Movie("Guardians of the Galaxy", 2012)
    watchlist.add_movie(m1)
    watchlist.add_movie(m2)
    watchlist.add_movie(m3)
    first = watchlist.first_movie_in_watchlist()
    assert first is m1
    i = iter(watchlist)
    assert next(i) is m1