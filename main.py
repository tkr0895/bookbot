def get_book_text(book):
    with open(book) as f:
        return f.read()
    
from stats import count_words

def main():
    word_count = count_words(get_book_text("./books/frankenstein.txt"))
    print(f"{word_count} words found in the document")

main()