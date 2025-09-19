def get_book_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents

# this is a read file example in practice
# the file object is named f
def count_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words
def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text) 
    print(f"{num_words} words found in the document")
main()