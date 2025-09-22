# python
def get_num_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words


def get_num_characters(book_text):
    char_counts= {}
    for char in book_text:
        lower_char = char.lower()
        if lower_char in char_counts:
            char_counts[lower_char] += 1
        else:
            char_counts[lower_char] = 1
    return char_counts
