def get_book_text(book):
    with open(book) as f:
        return f.read()

def main():
    print(get_book_text("./books/frankenstein.txt"))

main()