def get_word_count(book_text):
    return len(book_text.split())

def get_character_count(book_text):
    character_dict = {}
    for character in book_text:
        character = character.lower()
        character = str(character)
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1

    return character_dict

def sort_on(items):
    return items[1]

def dictionary_sorter(character_count):
    sorted_list = list(character_count.items())
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list