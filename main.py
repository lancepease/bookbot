def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")
    print()

    characters = count_characters(file_contents)
    sorted_chars = sorted(characters.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    characters = {}
    for char in text:
        if char.lower() not in characters:
            characters[char.lower()] = 1
        else:
            characters[char.lower()] += 1
    return characters


main()
