from stats import get_num_words
from stats import get_num_characters
from stats import convert_chars_to_sorted_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# The rest of your script for processing the book path would go here
# For example, to print the path:
# book_path = sys.argv[1]
# print(f"Processing book: {book_path}")

def get_book_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents

# this is a read file example in practice
# the file object is named f

def main():
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text) 
    char_counts = get_num_characters(book_text)
    sorted_char_list = convert_chars_to_sorted_list(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_list:
        ch = item["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {item['num']}")
    print("============= END ===============")
main()
