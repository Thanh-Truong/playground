#Write a method to replace all spaces in a string with %20
#
def replace_spaces(str):
    # Traverse the string from left to right
    # if it is a space, replace it with %20
    # then shift the string right to left until encountering non-space
    # or end of string
    array = list(str)
    length = len(array)
    for i in range(length):
        if array[i] == ' ': # space
            array[i] = '%20'
            # next character is space ?
            if (i + 1 < length) and (array[i + 1] == ' '):
                # move all right to left
                length -= 1
                for j in range(i + 1, length):
                    array[j] = array [j + 1]
    print("".join(array[:length]))
    return "".join(array[:length])

def main():
    assert replace_spaces(" A") == "%20A"
    assert replace_spaces(" A  ") == "%20A%20"
    assert replace_spaces(" A  B  CDEF ") == "%20A%20B%20CDEF%20"


if __name__ == "__main__":
    main()