# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
#  write a method to rotate the image by 90 degrees Can you do this in place?
import random

def make_array(n, m, default_value=None):
    return [
        # random
        [default_value if default_value else random.randint(0, 100) 
        for j in range(m)]
        for i in range(n)]

def print_array(array):
    for subarray in array:
        print(subarray)

def rotate(array):
    n = len(array)
    m = len(array[0])
    new_array = make_array(m, n, -1)
    for i in range(m):
        for j in range(n):
            new_array[i][j] = array[j][i]
    return new_array

def main():
    array = make_array(4, 3)
    print_array(array)
    print('---------------------')
    rotated_array = rotate(array)
    print_array(rotated_array)


if __name__ == "__main__":
    main()