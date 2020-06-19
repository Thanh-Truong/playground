def merge_sort(array):
    # Special cases
    if len(array) <= 1:
        return array
    # divide
    left = array[0: len(array)//2]
    right = array[len(array)//2:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    # merge two sorted arrays
    i = left_index = right_index = 0
    while (left_index < len(sorted_left) and right_index < len(sorted_right)):
        if sorted_left[left_index] <= sorted_right[right_index]:
            array[i] = sorted_left[left_index]
            left_index += 1
        else:
            array[i] = sorted_right[right_index]
            right_index += 1
        i += 1
    # left over ?
    while left_index < len(sorted_left):
        array[i] = sorted_left[left_index]
        left_index += 1
        i += 1
    while right_index < len(sorted_right):
        array[i] = sorted_right[right_index]
        right_index += 1
        i += 1
    return  array

def main():
    assert merge_sort([3, 4, 7, 1, 0, 90, 4]) == [0, 1, 3, 4, 4, 7, 90]
    assert merge_sort([3]) == [3]
    assert merge_sort([3,2]) == [2,3]
    assert merge_sort([]) == []
    
if __name__ == "__main__":
    main()