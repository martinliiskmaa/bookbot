import sys
from stats import get_book_text
from stats import number_of_words
from stats import letter_times
from stats import chars_dict_to_sorted_list



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    data = get_book_text(filepath)
    word_count = number_of_words(data)
    print(f"Found {word_count} total words")
    char_dict = letter_times(data)
    sorted_chars = chars_dict_to_sorted_list(char_dict)
    for item in sorted_chars:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
    return data

main()