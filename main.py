from stats import count_words, count_characters, split_and_sort_characters
import sys

def read_book_text(path_to_book):
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
    for character in character_count:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")
    print(f"============= END ===============")

def check_arguments(arguments):
    if len(arguments) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_word_count_and_char_list(booktext):
    word_count, words = count_words(booktext)
    char_count = count_characters(words)
    char_list = split_and_sort_characters(char_count)
    return word_count, char_list

def main():
    check_arguments(sys.argv)
    path_to_book = sys.argv[1]
    booktext = read_book_text(path_to_book)
    word_count, char_list = get_word_count_and_char_list(booktext)
    print_report(path_to_book, word_count, char_list)

main()