def count_words(booktext):
    words = booktext.split()
    return len(words)

def count_characters(booktext):
    characters_dict = {}
    words = booktext.split()
    for word in words:
        for c in word:
            c = c.lower()
            if c in characters_dict:
                characters_dict[c] += 1
            else:
                characters_dict[c] = 1
    return characters_dict

def split_dictionary(dict_in):
    list_out = []
    for k in dict_in:
        dict_out = {}
        dict_out["char"] = k
        dict_out["num"] = dict_in[k]
        list_out.append(dict_out)
    list_out = sort_list(list_out) 
    return(list_out)

def sort_list(lst):
    lst.sort(reverse=True, key=sort_on)
    return lst

def sort_on(dict):
    return dict["num"]
