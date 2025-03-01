def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def format_chars_dict(chars):
    chars_dict_list = []
    for i in chars:
        dict = {}
        dict['character'] = i
        dict['count'] = chars[i]
        chars_dict_list.append(dict)
    return chars_dict_list


def sort_on(chars_dict_list):
    return chars_dict_list['count']


def sort_chars_dict(chars_dict):
    formated_list = format_chars_dict(chars_dict)
    formated_list.sort(reverse=True, key=sort_on)
    return(formated_list)
