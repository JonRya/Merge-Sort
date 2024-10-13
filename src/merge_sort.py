# Main function
def merge_sort(unsorted_list: list[int]) -> list[int]:
    # Stop recusion when the unsorted list only has a length of 1
    if len(unsorted_list) == 1:
        return unsorted_list

    # Divide the unsorted list into two halves
    middle: int = len(unsorted_list) // 2
    # Use recursion to keep dividing each halves
    left: list[int] = merge_sort(unsorted_list[:middle])
    right: list[int] = merge_sort(unsorted_list[middle:])

    # Merge and sort both halves
    return merge(left, right)

# Merge function
def merge(left: list[int], right: list[int]) -> list[int]:
    merged: list[int] = []
    index_l: int = 0
    index_r: int = 0

    # Keep looping until all numbers are sorted
    while True:
        # If one of the index variables reach the end of their list
        # Append the remaining numbers from the other array and stop looping
        if index_l == len(left):
            merged.extend(right[index_r:])
            break
        elif index_r == len(right):
            merged.extend(left[index_l:])
            break
        
        # Sort and combine the numbers of each list
        if left[index_l] < right[index_r]:
            merged.append(left[index_l])
            index_l += 1
        else:
            merged.append(right[index_r])
            index_r += 1

    return merged


# Only for testing
if __name__ == '__main__':
    # Create an unsorted list
    from utils import create_unordered_list
    unsorted = create_unordered_list.create_unordered_list(1000)

    # Test and evaluate the result of the sorting function
    sorted_list = merge_sort(unsorted)
    print(sorted_list)
    assert sorted_list == sorted(unsorted)
