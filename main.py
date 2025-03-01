from stats import get_num_words, get_chars_dict, sort_chars_dict


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars_list = sort_chars_dict(chars_dict)
    
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for i in sorted_chars_list:
        if i['character'].isalpha():
            print(f'{i['character']}: {i['count']}')
    print('============= END ===============')


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()