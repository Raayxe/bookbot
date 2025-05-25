from stats import count_words, count_char, get_sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    novel = get_book_text(sys.argv[1])
    num_words = count_words(novel)
    char_dict = count_char(novel)
    sorted_list = get_sorted_list(char_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        print(f"{dict["char"]}: {dict["num"]}")
    

main()