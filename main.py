from stats import character_count, word_count, book_report
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        booktext = get_book_text(book_path)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print("----------- Word Count ----------")
        print(f"Found {word_count(booktext)} total words")
        print("--------- Character Count -------")
        characters = character_count(booktext)
        report = book_report(characters)
        for char in report:
            if char["char"].isalpha():
                print(f"{char["char"]}: {char["num"]}")
            else:
                pass
        print("============= END ===============")



main()
