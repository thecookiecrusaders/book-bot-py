
def main():
    book_path = "books/frankenstein.txt"  # Path to the book file
    book_contents = get_book_text(book_path)
    num_words = get_word_count(book_contents)
    print(f"Found {num_words} total words")

def get_book_text(path: str) -> str:
    with open(path, "r") as file:
        file_contents = file.read()
        return file_contents

def get_word_count(book_text: str) -> int:
    words = book_text.split()
    return len(words)

if __name__ == "__main__":
    main()