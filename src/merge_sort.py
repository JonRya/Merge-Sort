from utils import create_unordered_list


# Main function
def merge_sort(unsorted_list: list[int]) -> list[int]:
    if len(unsorted_list) == 1:
        return unsorted_list

    middle: int = len(unsorted_list) // 2
    left: list[int] = merge_sort(unsorted_list[:middle])
    right: list[int] = merge_sort(unsorted_list[middle:])

    return merge(left, right)

def merge(left: list[int], right: list[int]) -> list[int]:
    merged: list[int] = []
    index_l: int = 0
    index_r: int = 0

    while True:
        if index_l == len(left):
            merged.extend(right[index_r:])
            break
        elif index_r == len(right):
            merged.extend(left[index_l:])
            break
        
        if left[index_l] < right[index_r]:
            merged.append(left[index_l])
            index_l += 1
        else:
            merged.append(right[index_r])
            index_r += 1

    return merged


# Only for testing
if __name__ == '__main__':
    unsorted = create_unordered_list.create_unordered_list(1000)
    sorted_list = merge_sort(unsorted)
    print(sorted_list)
    assert sorted_list == sorted(unsorted)
