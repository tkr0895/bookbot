def get_book_text(book):
    with open(book) as f:
        return f.read()

def count_words(booktext):
    words = booktext.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def main():
    word_count = count_words(get_book_text("./books/frankenstein.txt"))
    print(f"{word_count} words found in the document")

main()