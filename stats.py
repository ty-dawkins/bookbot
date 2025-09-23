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
#sort helper function
def sort_on(char_counts):
    return char_counts["num"]
    
letters = [
    {"char": "a", "num": 25894},
    {"char": "b", "num": 4868},
    {"char": "c", "num": 9011},
    ]
letters.sort(reverse=True, key=sort_on)
print(letters)

#A NEW main function- this converts the character dictionary to a list and uses sort_on to sort it
def convert_chars_to_sorted_list(char_counts):
    char_counts_list = []
    for char, num in char_counts.items():
        char_counts_list.append({"char": char, "num": num})
    char_counts_list.sort(reverse=True, key=sort_on)
    return char_counts_list
