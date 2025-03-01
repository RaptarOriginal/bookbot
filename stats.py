def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_counts(text):
    lowercase_text = text.lower()
    character_count = {}
    characters = list(lowercase_text)
    for char in characters:
        if char not in character_count:
            character_count[char] = 1
        else:
            character_count[char] += 1
    return character_count