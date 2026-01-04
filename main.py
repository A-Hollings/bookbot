from stats import get_word_count, get_character_count, dictionary_sorter
import sys

def get_book_text(filepath):
    with open(filepath, mode='r', encoding='utf-8-sig') as f:
        file_contents = f.read()
        return file_contents

def main():
    print('Usage: python3 main.py <path_to_book>')
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    sorted_list = dictionary_sorter(character_count)
    sorted_dict = dict(sorted_list)
    print('============ BOOKBOT ============')
    print(f'Analysing book found at {filepath}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for key, value in sorted_dict.items():
        if key[0].isalpha():
            print(f'{key}: {value}')
    print('============= END ===============')

main()

