
def word_count(file_string):
    words = file_string.split()
    count = 0
    for word in words:
        count+=1
    return count

def character_count(og_string):
    string = og_string.lower()
    words = string.split()
    characters = {}
    for word in words:
        for character in word:
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1
    return characters

def sort_on(items):
    return items["num"]

def book_report(char_dict):
    new_list = []
    for key, value in char_dict.items():
        new_list.append({"char": key, "num": value})
    new_list.sort(reverse=True, key=sort_on)
    return new_list
