import argparse
import sys

from data_initializer import DataCSVInitializer
from data_operations import DataOperations


class DataSearcher:
    def __init__(self):
        parser = argparse.ArgumentParser()
        argument_group = parser.add_mutually_exclusive_group()

        argument_group.add_argument("--sort_by", required=False, help='Sorting all movies by every column')
        argument_group.add_argument("--filter_by", nargs='+', required=False,
                                    help='Filtering by arguments:'
                                         'director, '
                                         'actor,'
                                         'nominated for Oscar but did not win,'
                                         'won more than 80% of nominations,'
                                         'earn more than 100 000 000 $,'
                                         'movies in certain language')
        argument_group.add_argument("--compare", nargs='+', required=False,
                                    help='Comparing by:'
                                         'IMDb Rating,'
                                         'box office earnings,'
                                         'number of awards won,'
                                         'runtime')
        argument_group.add_argument("--add", required=False, help='Adding new movie to data source')
        argument_group.add_argument("--highscores", nargs='?', required=False,
                                    help='Showing current highscores in:'
                                         'runtime,'
                                         'box office earnings,'
                                         'most awards won,'
                                         'most nominations,'
                                         'most Oscars,'
                                         'highest IMDB Rating.')
        self.args = parser.parse_args()
        self.operations = DataOperations()

    def process_args(self, data):
        result = []
        if len(sys.argv) <= 1:
            result = 'No args given'
        try:
            if self.args.sort_by is not None:
                result = self.operations.sort_by_column(data, self.args.sort_by)
            if self.args.filter_by is not None:
                result = self.operations.filter_by_attribute(data, self.args.filter_by[0], self.args.filter_by[1])
            if self.args.compare is not None:
                result = self.operations.compare(data, self.args.compare[0], self.args.compare[1], self.args.compare[2])
            if self.args.add is not None:
                result = self.operations.add_movie(data, self.args.add)
            if self.args.highscores is not None:
                result = self.operations.show_most(data)
            print(result)
        except AttributeError as e:
            print('Error: ', e)
