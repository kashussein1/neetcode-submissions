from typing import List # this is used to add type hints for List type

def remove_from_list(my_list: List[int], index: int) -> List[int]:
    length = len(my_list)
    for i in range(0, length):
        if i == index:
            my_list.pop(i)
    return my_list

def pop_n_from_list(my_list: List[int], n: int) -> List[int]:
    length = len(my_list) -1
    count =0
    for i in range(length, length - n, -1):
        my_list.pop(i)
    return my_list

# don't modify below this line
print(remove_from_list([1, 2, 3, 4, 5], 2))
print(remove_from_list([1, 2, 3, 4, 5], 0))
print(remove_from_list([1, 2, 3, 4, 5], 4))

print(pop_n_from_list([1, 2, 3, 4, 5], 2))
print(pop_n_from_list([1, 2, 3, 4, 5], 0))
print(pop_n_from_list([1, 2, 3, 4, 5], 5))
