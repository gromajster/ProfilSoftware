# Profil software intern task

Variable fetch_from_api, should be set to true to fetch data from service if is false it should load data from api or local file.

Functions:
--
--sort_by {id, tittle, runtime, genre, director, cast, writer, language, country, awards, imdb_rating,
                 imdb_votes, box_office}

Sorting all movies by every column

--filter_by {director,actor,language} {"attr"}

--filter_by {box_office,awards_won,awards_nom} 

'Filtering by arguments:'
                                         'director, '
                                         'actor,'
                                         'nominated for Oscar but did not win,'
                                         'won more than 80% of nominations,'
                                         'earn more than 100 000 000 $,'
                                         'movies in certain language'

--compare {imdb_rating, box_office, awards, runtime} {"movie_1"} {"movie_2"}

'Comparing by:'
                                         'IMDb Rating,'
                                         'box office earnings,'
                                         'number of awards won,'
                                         'runtime'

--add {"movie_tittle"}

'Adding new movie to data source'

--highscores 

'Showing current highscores in:'
                                         'runtime,'
                                         'box office earnings,'
                                         'most awards won,'
                                         'most nominations,'
                                         'most Oscars,'
                                         'highest IMDB Rating.'