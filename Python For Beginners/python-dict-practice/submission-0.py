from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    char_count = {}
    for char_1 in word:
        count = 0
        if char_1 not in char_count:
            for char_2 in word:
                if char_1 == char_2:
                    count +=1
            char_count[char_1] = count
    return char_count


# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
