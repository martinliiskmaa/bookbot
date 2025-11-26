from stats import number_of_words
from stats import letter_times


def main():
    FILEPATH = "books/frankenstein.txt"
    data = get_book_text(FILEPATH)
    word_count = number_of_words(data)
    print(f"Found {word_count} total words")
    char_dict = letter_times(data)
    return data


def get_book_text(filepath):
    with open(filepath, "r") as file:
        data = file.read()
    return data


main()
