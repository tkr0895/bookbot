from stats import count_words
from stats import count_characters
from stats import split_dictonary
import sys

def get_book_text(book):
    with open(book) as f:
        return f.read()
    
def print_report(path, total_words, character_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print(f"--------- Character Count -------")
    for dict in character_count:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

def check_arguments(arguments):
    if len(arguments) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    check_arguments(sys.argv)
    path = sys.argv[1]
    word_count = count_words(get_book_text(path))
    char_count = count_characters(get_book_text(path))
    char_list = split_dictonary(char_count)
    print_report(path, word_count, char_list)

main()