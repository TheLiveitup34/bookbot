import shlex
import sys
def sort_on(dict):
    return dict['num']

def number_of_words(text):
    return len(text.split())
def number_of_letters(text):
    text = text.lower()
    letters = {}
    letters_final = []
    for char in text:
        if char not in letters and char.isalpha():
            letters[char] = 1
        elif char.isalpha():
            letters[char] +=1
    for letter in letters:
        letters_final.append({"name": letter, "num": letters[letter]})       
    return letters_final

def main() -> int:
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        letters = number_of_letters(file_contents)
        letters.sort(reverse=True, key=sort_on)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{number_of_words(file_contents)} words found in the doucment")
        print("")
        for letter in letters:
            print(f"The {letter['name']} character was found {letter['num']} times")
        print("--- End report ---")
    return 0


if __name__ == '__main__':
    sys.exit(main())