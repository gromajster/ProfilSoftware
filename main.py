from data_initializer import DataCSVInitializer
from data_searcher import DataSearcher
import os


def main():
    fetch_from_api = os.environ['FETCH_FROM_API']
    data = DataCSVInitializer().load_data(fetch_from_api)
    DataSearcher().process_args(data)


if __name__ == '__main__':
    main()
