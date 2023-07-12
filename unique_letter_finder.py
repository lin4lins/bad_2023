import re

from cli import get_arguments, get_text_from_file


class Word:
    def __init__(self, word: str):
        self.__letters = [letter for letter in word]

    def get_first_unique_letter(self) -> str:
        """
        Based on letters and their appearance frequencies identifies the first letter that occurs only once in a word.
        Returns: a string, which is the first unique letter
                 or an empty string in case a word does not have any unique letters.

        """
        letter_frequency = self.__get_letters_frequency()
        for letter, frequency in letter_frequency.items():
            if frequency == 1:
                return letter

        return ""

    def __get_letters_frequency(self) -> dict:
        """
        Iterates through a letters list and counts how many times each letter appeared in the word.
        Returns: a dict with the letters and their appearance frequencies.

        """
        letter_frequency = {}
        for letter in self.__letters:
            current_frequency = letter_frequency.get(letter, 0)
            letter_frequency[letter] = current_frequency + 1

        return letter_frequency


class Text:
    def __init__(self, text: str):
        self.__words = []
        self.__define_words(text)

    def get_first_unique_letter(self) -> str:
        """
        Based on first unique letters of all the words of the text defines which letter was the first unique
        in a whole text.
        Returns: a string, which is the first unique letter
                 or an empty string in case a text does not have any unique letters.

        """
        unique_letters_string = self.__get_unique_letters_string()
        return Word(unique_letters_string).get_first_unique_letter()

    def __define_words(self, text: str) -> None:
        """
        Defines which words there are in a text.
        Args:
            text: a string with a text

        Returns: None

        """
        raw_words = text.split()
        word_without_non_alphanum = [re.sub(r"\W", "", word) for word in raw_words]
        self.__words = [Word(word) for word in word_without_non_alphanum]

    def __get_unique_letters_string(self) -> str:
        """
        Iterates through a words list and writes down the first unique letter of every word to a string.
        Returns: a string with first unique letters of all the words of the text

        """
        unique_letters_string = ""
        for word in self.__words:
            unique_letters_string += word.get_first_unique_letter()

        return unique_letters_string


def run_cli_app():
    """
    Runs a command-line interface (CLI) application to process text from a file and find the first unique letter.
    Returns: None

    """
    arguments = get_arguments()
    text_from_file = get_text_from_file(arguments.path) if arguments.path else None
    text = Text(text_from_file)
    result = text.get_first_unique_letter()
    if result:
        print(f"The unique letter of the text is '{result}'.")
        return

    print(f"The text does not have an unique letter.")


if __name__ == "__main__":
    run_cli_app()
