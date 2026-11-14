from logger import get_logger
from input_reader import read_csv_file
from exception import InputFileError

logger = get_logger(__name__)


def main():

    logger.info("Tournament backend started")

    try:
        data = read_csv_file("data/input/demo.csv")

        logger.info("Input file loaded successfully")

        print(data)

    except FileNotFoundError as error:

        logger.error(f"Input file error: {error}")

    except Exception as error:

        logger.error(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()