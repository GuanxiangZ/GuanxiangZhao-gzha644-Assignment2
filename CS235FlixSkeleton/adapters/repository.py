import abc
from typing import List

from CS235FlixSkeleton.domainmodel.model import User, Movie, Actor, Director, Genre, Review


repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_user(self, user: User):
        """" Adds a User to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username) -> User:
        """ Returns the User named username from the repository.

        If there is no User with the given username, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_actor(self, actor: Actor):
        """" Adds an Actor to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_actor(self) -> List[Actor]:
        """ Returns the Actor stored in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def add_director(self, director: Director):
        """" Adds a Director to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_director(self) -> List[Director]:
        """ Returns the Director stored in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        """" Adds a Genre to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_genre(self) -> List[Genre]:
        """ Returns the Genre stored in the repository. """
        raise NotImplementedError


###review 双链



    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        """" Adds a Movie to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, id : int) -> Movie:
        """ Returns Movie with id from the repository.

        If there is no Article with the given title and year, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_page(self, page: int) -> List[Movie]:
        """ Returns a list of Movies that were published on page.

        If there are no Articles on the given date, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_page_of_previous_movie(self, movie: Movie):
        """ Returns the date of an Movie that immediately precedes article.

        If article is the first Article in the repository, this method returns None because there are no Articles
        on a previous date.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_page_of_next_movie(self, movie: Movie):
        """ Returns the date of an Article that immediately follows article.

        If article is the last Article in the repository, this method returns None because there are no Articles
        on a later date.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_movies(self):
        """ Returns the number of Movie in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_movie(self) -> Movie:
        """ Returns the first Movie, ordered by date, from the repository.

        Returns None if the repository is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_movie(self) -> Movie:
        """ Returns the first Movie, ordered by date, from the repository.

        Returns None if the repository is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_next_movie(self):

        raise NotImplementedError



