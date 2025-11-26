def number_of_words(data):
    num = len(data.split())
    return num

def letter_times(data):
    data = data.lower()
    new_dict = {}
    for char in data:
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1
    print(new_dict)
    return new_dict



