import argparse


def set_arguments():
    parser = argparse.ArgumentParser(
        description="Get the first unique letter of the text in the file")
    parser.add_argument("--file", type=str, dest="path")
    return parser


def get_arguments():
    parser = set_arguments()
    arguments = parser.parse_args()
    return arguments


def get_text_from_file(path: str):
    with open(path, 'r') as file:
        return file.read()
