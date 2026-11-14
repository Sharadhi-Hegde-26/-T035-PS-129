from logger import get_logger
from input_reader import read_csv_file
from config import get_input_path

logger = get_logger(__name__)


def main():

    logger.info("Tournament backend started")

    try:
        # Get input file path from config
        file_path = get_input_path("demo.csv")

        # Read CSV file
        data = read_csv_file(file_path)

        logger.info("Input file loaded successfully")

        print("\nTournament Data:")
        print(data)

        logger.info("Backend execution completed")

    except FileNotFoundError as error:
        logger.error(f"File error: {error}")

    except ValueError as error:
        logger.error(f"Data error: {error}")


if __name__ == "__main__":
    main()