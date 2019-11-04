import requests
import csv

from movie_class import movieClass


class DataCSVInitializer:

    def load_data(self, fetch_from_api):
        movies = []
        if fetch_from_api == 'true':
            movies = self.fetch_data_from_api()
            self.save_to_csv(movies)
            return movies
        else:
            return self.load_from_csv()

    def fetch_data_from_api(self):
        my_list = []
        with open('Backend_movies.csv', 'r', encoding="UTF-8") as f:
            next(f)
            reader = csv.reader(f, delimiter=",")
            session = requests.Session()
            for row in reader:
                response = session.get("http://www.omdbapi.com/?apikey=9dd13c74&t=" + row[1])
                my_list.append(
                    movieClass(int(row[0]), response.json()['Title'], response.json()['Runtime'],
                               response.json()['Genre'],
                               response.json()['Director'], response.json()['Actors'], response.json()['Writer'],
                               response.json()['Language'], response.json()['Country'], response.json()['Awards'],
                               float(response.json()['imdbRating']), response.json()['imdbVotes'],
                               response.json().get('BoxOffice', "N/A")))

        return my_list

    def load_from_csv(self):
        with open('Backend_movies.csv', 'r') as f:
            my_list = []
            next(f)
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                my_list.append(
                    movieClass(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                               row[10], row[11], row[12]))
            return my_list

    def save_to_csv(self, movies):
       pass

