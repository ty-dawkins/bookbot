from stats import get_num_words
def get_book_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents

# this is a read file example in practice
# the file object is named f

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text) 
    print(f"{num_words} words found in the document")
main()
