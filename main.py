PATH_FRANKENSTEIN = "books/frankenstein.txt"

def get_book_text():
    with open(PATH_FRANKENSTEIN) as f:
        file_content = f.read()

    return file_content

def count_words(book):
    words_list = book.split()

    return len(words_list)

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    sorted_list = []
    for c in dict:
        sorted_list.append({"char": c, "num": dict[c]})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list


def count_characters(book):
    char_count = {}
    for char in book.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] +=1

    return char_count

def main():

    book = get_book_text()
    num_words = count_words(book)

    char_count = count_characters(book)
    char_sort_list = sort_dict(char_count)

    print(f"--- Report of {PATH_FRANKENSTEIN} ---")
    print(f"{num_words} words found in the document.")
    for item in char_sort_list:
        if item["char"].isalpha():
            print(f"The '{item["char"]}' character was found {item["num"]} times")
    print("--- End of report ---")


if __name__ == "__main__":
    main()