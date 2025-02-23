def count_words(booktext):
    words = booktext.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def count_characters(booktext):
    characters = {}
    words = booktext.split()
    for word in words:
        for c in word:
            c = c.lower()
            if c in characters:
                characters[c] += 1
            else:
                characters[c] = 1
    return characters