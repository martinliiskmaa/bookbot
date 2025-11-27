def get_book_text(filepath):
    with open(filepath, "r") as file:
        data = file.read()
    return data


def number_of_words(data):
    num = len(data.split())
    return num


def letter_times(data):
    data = data.lower()
    char_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
                 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
                 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
                 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
                 'u': 0, 'v': 0,}
    for char in data:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict


def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(char_dict):
    sorted_list = []
    for ch in char_dict:
        sorted_list.append({"char": ch, "num": char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list





