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