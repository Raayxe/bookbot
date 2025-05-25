def count_words(file):
    words = file.split()
    return len(words)

def count_char(file):
    char_dict = {}
    for c in file:
        c = c.lower()
        if c.isalpha():
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1  
    return char_dict

def sort_on(dict):
    return dict["num"]

def get_sorted_list(char_dict):
    list_of_dict = []
    for d in char_dict:
        new_dict = {}
        new_dict["char"] = d
        new_dict["num"] = char_dict[d]
        list_of_dict.append(new_dict)
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict





