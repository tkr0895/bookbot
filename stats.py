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

def split_dictonary(dict_in):
    list_out = []
    for k in dict_in:
        dict_out = {}
        dict_out["char"] = k
        dict_out["num"] = dict_in[k]
        list_out.append(dict_out)
    return(list_out)
