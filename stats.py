def get_num_words(book_text: str) -> int:
    words = book_text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

    
def dict_to_list(char_counts):
    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})
    return char_list

def sort_on(item):
    return item["num"]