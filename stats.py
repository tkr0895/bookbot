def count_words(booktext):
    words = booktext.split()
    return len(words), words

def count_characters(words):
    characters_dict = {}
    for word in words:
        for c in word:
            c = c.lower()
            if c in characters_dict:
                characters_dict[c] += 1
            else:
                characters_dict[c] = 1
    return characters_dict

def split_and_sort_characters(char_dict):
    char_list = [{"char": k, "num": v} for k, v in char_dict.items()]
    return sorted(char_list, reverse=True, key=lambda x: x["num"])
