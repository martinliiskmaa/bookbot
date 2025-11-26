def number_of_words(data):
    num = len(data.split())
    return num


def letter_times(data):
    data = data.lower()
    char_dict = {}
    for char in data:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sorting(char_dict):
    new_list = []
    for char, count in char_dict.items():
        if char in char_dict:
            new_list.append(char)





