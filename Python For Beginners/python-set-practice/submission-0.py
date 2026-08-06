from typing import List

def contains_duplicate(words: List[str]) -> bool:
    words_set_length = len(set(words))  
    return words_set_length != len(words)

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
