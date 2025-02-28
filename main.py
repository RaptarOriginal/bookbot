def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def word_count(book_text):
    num_words = 0
    words = book_text.split()
    for word in words:
        num_words += 1
    
    return num_words

def main():
    book_text = get_book_text('books/frankenstein.txt')
    num_words = word_count(book_text)

    print(f'{num_words} words found in the document')

main()