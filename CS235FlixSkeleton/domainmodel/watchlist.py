from CS235FlixSkeleton.domainmodel.model import Movie

class WatchList:
    def __init__(self):
        self.__watchlist = []
        self.__id = 0

    def add_movie(self, movie: Movie):
        if isinstance(movie, Movie):
            if movie not in self.__watchlist:
                movie.id = self.__id
                movie.page = self.__id // 10
                self.__id += 1
                self.__watchlist.append(movie)

    def remove_movie(self, movie: Movie):
        if isinstance(movie, Movie):
            if movie in self.__watchlist:
                self.__watchlist.remove(movie)

    def select_movie_to_watch(self, index: int):
        if isinstance(index, int):
            if index >= 0 and index < len(self.__watchlist):
                return self.__watchlist[index]
            else:
                return None

    def select_movie_by_page(self, page: int):
        movies = []
        print(page)
        for movie in self.__watchlist:
            if movie.page == int(page):
                movies.append(movie)
        return movies

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        if self.__watchlist == []:
            return None
        else:
            return self.__watchlist[0]

    def last_movie_in_watchlist(self):
        if self.__watchlist == []:
            return None
        else:
            return self.__watchlist[-1]

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.__watchlist):
            ob = self.__watchlist[self.n]
            self.n += 1
            return ob
        else:
            return None