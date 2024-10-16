def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        letter_count = {}
        file_contents = f.read()
        word_count = len(file_contents.split())
        file_contents = file_contents.lower()
        for letter in file_contents:
            if letter in letter_count:
                letter_count[letter] +=1
            elif letter.isalpha():
                letter_count[letter] = 1
        print(f"--- Begin Report of {path} ---")
        print(f"{word_count} words were found in the document")
        print("\n")
        for letter in letter_count:
            print(f"The '{letter}' character was found {letter_count[letter]} times")
        print("--- End Report ---")


main()