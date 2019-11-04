import operator
import requests

from movie_class import movieClass


class DataOperations:

    def sort_by_column(self, movies, column):
        self._validate_attribute(column, movies[0])
        sorted_list = sorted(movies, key=operator.attrgetter(column))
        return sorted_list

    def filter_by_attribute(self, movies, column, data_2=None):
        if column == 'awards_nom':
            return self._nominated_but_not_win(movies)
        elif column == 'awards_nom':
            return self._win_more_than_80(movies)
        elif column == 'box_office':
            result = self._filter_box_office(movies, 100000000)
            return result
        else:
            self._validate_attribute(column, movies[0])
            getter = operator.attrgetter(column)
            new_list = filter(lambda x: data_2 in getter(x), movies)
            return new_list

    def compare(self, movies, column, movie_1, movie_2):
        self._validate_attribute(column, movies[0])
        getter = operator.attrgetter(column)
        movie_one = list(filter(lambda x: x.tittle == movie_1, movies))
        movie_two = list(filter(lambda x: x.tittle == movie_2, movies))
        if column == "awards":
            result = self._more_awards(getter, movie_one, movie_two)
            return result
        else:
            result = self._choose_greater_int(column, getter, movie_one, movie_two)
            return result

    def add_movie(self, movies, movie):
        response = requests.get("http://www.omdbapi.com/?apikey=9dd13c74&t=" + movie)
        index = movies[-1].id + 1
        if response.status_code == 200:
            movies.append(
                movieClass(index, response.json()['Title'], response.json()['Runtime'], response.json()['Genre'],
                           response.json()['Director'], response.json()['Actors'], response.json()['Writer'],
                           response.json()['Language'], response.json()['Country'], response.json()['Awards'],
                           response.json()['imdbRating'], response.json()['imdbVotes'],
                           response.json().get('BoxOffice', "N/A")))
            return movies
        else:
            return "Wrong title"

    def show_most(self, movies):
        highscores = []
        runtime = 0
        box_office = 0
        nominations = 0
        oscars = 0
        rating = 0

        for row in movies:
            if self._time_parser(row.runtime) > runtime:
                runtime = self._time_parser(row.runtime)
                title1 = row.title
            if self._cash_parser(row.box_office) > box_office:
                box_office = self._cash_parser(row.box_office)
                title2 = row.title
            if row.imdb_rating > rating:
                rating = row.imdb_rating
                title3 = row.title
            if self._nominations(row.awards) > nominations:
                nominations = self._nominations(row.awards)
                title4 = row.title
            if self._oscars(row.awards) > oscars:
                oscars = self._oscars(row.awards)
                title5 = row.title
        highscores.append([title1, runtime])
        highscores.append([title2, box_office])
        highscores.append([title3, rating])
        highscores.append([title4, nominations])
        highscores.append([title5, oscars])

        return highscores

    ##############################################################################################
    def _validate_attribute(self, column, clazz):
        if not hasattr(clazz, column):
            raise AttributeError("Wrong attribute passed to the program")

    def _time_parser(self, time):
        (t, minutes) = time.split(' ')
        return int(t)

    def _cash_parser(self, cash):
        c = cash[1:].replace(",", "")
        return int(c)

    def _choose_greater_int(self, column, getter, movie_one, movie_two):
        if column == "runtime":
            var1 = self._time_parser(getter(movie_one[0]))
            var2 = self._time_parser(getter(movie_two[0]))
        elif column == "box_office":
            var1 = self._cash_parser(getter(movie_one[0]))
            var2 = self._cash_parser(getter(movie_two[0]))
        elif column == "imdb_rating":
            var1 = getter(movie_one[0])
            var2 = getter(movie_two[0])
        if var1 > var2:
            return movie_one
        else:
            return movie_two

    def _more_awards(self, getter, movie_one, movie_two):

        var1 = getter(movie_one[0])
        var2 = getter(movie_two[0])

        result_movie_one = self._splitting_words(var1)
        result_movie_two = self._splitting_words(var2)

        if result_movie_one > result_movie_two:
            return movie_one
        else:
            return movie_two

    def _splitting_words(self, var1):
        var = 0
        word_1 = "Won"
        word_2 = "wins"
        splitted_var = var1.split(" ")
        if word_1 in splitted_var and word_2 in splitted_var:
            var += int(splitted_var[splitted_var.index(word_1) + 1])
            var += int(splitted_var[splitted_var.index(word_2) - 1])
            return var
        elif word_1 in splitted_var:
            var += int(splitted_var[splitted_var.index(word_1) + 1])
            return var
        elif word_2 in splitted_var:
            var += int(splitted_var[splitted_var.index(word_2) - 1])
            return var

    def _filter_box_office(self, movies, minimum_box_office):
        new_list = []
        for row in movies:
            cash_parser = self._cash_parser(row.box_office)
            if cash_parser > minimum_box_office:
                new_list.append(row)
        return new_list

    def _nominated_but_not_win(self, movies):
        return [movie for movie in movies if "Nominated" in movie.awards]

    def _win_more_than_80(self, movies):
        result = []
        word_1 = "wins"
        word_2 = "nominations."
        for row in movies:
            if word_1 in row.awards and word_2 in row.awards:
                splitted_awards = row.awards.split(" ")
                a = float(splitted_awards[splitted_awards.index(word_1) - 1])
                b = float(splitted_awards[splitted_awards.index(word_2) - 1])
                if a / b * 100 >= 80.0:
                    result.append(row)
        return result

    def _oscars(self, oscars):
        result = 0
        osc = oscars.split(" ")
        word_1 = "Oscar"
        word_2 = "Oscars"
        if word_1 in osc:
            result = osc[osc.index(word_1) - 1]
            return result
        elif word_2 in osc:
            result = osc[osc.index(word_2) - 1]
            return result

    def _nominations(self, nomination):
        result = 0
        nom = nomination.split(" ")
        word_1 = "nominations"
        if word_1 in nom:
            result = nom[nom.index(word_1) - 1]
            return result
