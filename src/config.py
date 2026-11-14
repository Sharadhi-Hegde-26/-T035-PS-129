import os

# Project root directory
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Input and output directories
INPUT_DIR = os.path.join(BASE_DIR, "data", "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "data", "output")


def get_input_path(filename):
    return os.path.join(INPUT_DIR, filename)


def get_output_path(filename):
    return os.path.join(OUTPUT_DIR, filename)