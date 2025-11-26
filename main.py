def main():
    FILEPATH = "books/frankenstein.txt"
    data = get_book_text(FILEPATH)
    return data

def get_book_text(filepath):
    with open(filepath, "r") as file:
        data = file.read()
    return data



def number_of_words(data):
    num = len(data.split())
    print(f"Found {num} total words")


number_of_words(main())

