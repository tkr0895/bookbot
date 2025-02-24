from stats import count_words, count_characters, split_dictionary
import sys

def read_book_text(path_to_book):
    check_arguments(sys.argv)
    try:
        with open(path_to_book) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {path_to_book}")
    
def print_report(path, total_words, character_count):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print(f"--------- Character Count -------")
    for dict in character_count:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print(f"============= END ===============")

def check_arguments(arguments):
    if len(arguments) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_word_count_and_char_list(booktext):
    word_count = count_words(booktext)
    char_count = count_characters(booktext)
    char_list = split_dictionary(char_count)
    return word_count, char_list

def main():
    path_to_book = sys.argv[1]
    booktext = read_book_text(path_to_book)
    word_count, char_list = get_word_count_and_char_list(booktext)
    print_report(path_to_book, word_count, char_list)

main()