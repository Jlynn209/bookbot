def get_word_count_in_book(book_text) -> int:
    words = book_text.split()
    return len(words)


def get_repeated_characters(book_text) -> dict:
    repeated_chars = {}
    for char in book_text:
        if char == ' ':
            continue
        if repeated_chars.get(char.lower()):
            repeated_chars[char.lower()] += 1
        else:
            repeated_chars[char.lower()] = 1
    return repeated_chars


def sort_dictionary_by_value(input_dict: dict) -> list:
   list_of_keys_and_values = list(input_dict.items())
   list_of_keys_and_values.sort(key=lambda item: item[1], reverse=True)
   return list_of_keys_and_values

