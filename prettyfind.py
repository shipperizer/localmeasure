#!/usr/bin/env python3


def findsub(word, search):
    occurs = []
    for i, char in enumerate(word):
        if i + len(search) <= len(word) and char == search[0]:
            if word[i:i+len(search)] == search:
                occurs.append(i)
    return occurs


def findall(text, search):
    occurs = []
    index = 1
    textSearch = text.lower().split()
    searchWord = search.lower()
    for word in textSearch:
        if word == searchWord:
            occurs.append(index)
        elif searchWord in word:
            for occur in findsub(word, searchWord):
                occurs.append(index + occur)
        # adding word length plus the space
        index += len(word) + 1
    return occurs


def prettyfind(text, search):
    occurencies = [str(i) for i in findall(text, search)]

    print('Text:', text)
    print('Word: ', search)
    if occurencies:
        print('Result:', ' '.join(occurencies))
    else:
        print('Result: <No output>')


if __name__ == "__main__":
    text = input("Insert text to search: ")
    word = input("Insert word to look for: ")
    prettyfind(text, word)
