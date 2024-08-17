def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    num_chars = get_num_chars(text)
    print(num_chars)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)
 

def get_num_chars(text: str):
    charmap = {}
    # Test with just 100 characters for now
    lowered_text = text.lower()
    for char in lowered_text:
        if not charmap.get(char):
            charmap[char] = 1
            continue
        charmap[char] += 1
    return charmap


main()
