from stats import get_num_words, count_characters, dict_to_list, sort_on
import sys



def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]  # Path to the book file
    book_contents = get_book_text(book_path)
    num_words = get_num_words(book_contents)
    char_count_dict = count_characters(book_contents)
    print_pretty_header(book_path)
    print_pretty_word_count(book_contents)
    print_pretty_char_dict_count(char_count_dict, book_contents)
    print_pretty_tail()

def print_pretty_header(book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

def print_pretty_word_count(book_contents):
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_contents)} total words")

def print_pretty_char_dict_count(char_count_dict, book_contents):
    print("--------- Character Count -------")
    counts = count_characters(book_contents)
    char_list = dict_to_list(counts)
    char_list.sort(reverse=True, key=sort_on)
    for key in char_list:
        print(f"{key["char"]}: {key["num"]}")

def print_pretty_tail():
    print("============= END ===============")

def get_book_text(path: str) -> str:
    with open(path, "r") as file:
        file_contents = file.read()
        return file_contents




def print_char_dict_count(char_count_dict):
    for char in char_count_dict:
        print(f"{char}: {char_count_dict[char]}")

if __name__ == "__main__":
    main()