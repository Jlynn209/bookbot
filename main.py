import sys
from stats import get_word_count_in_book
from stats import get_repeated_characters
from stats import sort_dictionary_by_value


def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f" Found {get_word_count_in_book(book_text)} total words")
    print("--------- Character Count -------")
    repeated_char_dict = get_repeated_characters(book_text)
    for item in sort_dictionary_by_value(repeated_char_dict):
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")
    print("============= END ===============")

if __name__ == '__main__':
    main()