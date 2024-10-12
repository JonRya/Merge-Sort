# Creates a list with n amount of numbers and shuffles its content
import random

def create_unordered_list(n: int) -> list[int]:
    # list with n amount of numbers using list comprehension
    initial_list = [x for x in range(1, n+1)]

    # Shuffles the numbers in the list by iterating over the initial list
    # and inserting each number into a random index in a new list
    unordered_list = []
    for x in initial_list:
        if len(unordered_list) == 0:
            index = 0 # Index 0 if list is empty
        else:
            # Otherwise get a random possible index instead
            index = random.randint(0, len(unordered_list)-1)

        unordered_list.insert(index, x)

    return unordered_list


# Tests if the unordered list contains exactly n amount of numbers
if __name__ == '__main__':
    n = random.randint(100, 1000)
    unordered_list = create_unordered_list(n)
    assert(len(unordered_list) == n)
    print(f'{unordered_list}\nn = {n}')
