from stats import count_words
from stats import count_characters
from stats import split_dictonary

def get_book_text(book):
    with open(book) as f:
        return f.read()

def main():
    word_count = count_words(get_book_text("./books/frankenstein.txt"))
    char_count = count_characters(get_book_text("./books/frankenstein.txt"))
    char_list = split_dictonary(char_count)
    print(f"{word_count} words found in the document")
    print(char_list)

main()