class movieClass:
    def __init__(self, id, tittle, runtime, genre, director, cast, writer, language, country, awards, imdb_rating,
                 imdb_votes, box_office):
        self.id = id
        self.tittle = tittle
        self.runtime = runtime
        self.genre = genre
        self.director = director
        self.cast = cast
        self.writer = writer
        self.language = language
        self.country = country
        self.awards = awards
        self.imdb_rating = imdb_rating
        self.imdb_votes = imdb_votes
        self.box_office = box_office

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.id!r}, '
                f'{self.tittle!r},'
                f'{self.runtime!r}, '
                f'{self.genre!r}, '
                f'{self.director!r}, '
                f'{self.cast!r}, '
                f'{self.writer!r}, '
                f'{self.language!r}, '
                f'{self.country!r}, '
                f'{self.awards!r}, '
                f'{self.imdb_rating!r}, '
                f'{self.imdb_votes!r}, '
                f'{self.box_office!r})')