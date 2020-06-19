#Write a method to decide if two strings are anagrams or not

def is_anagrams(stra, strb):
    # Solution 1. return sort(stra) == sort(strb)
    # Solution 2. a number of occurence of every character in stra is the same in strb
    #   da = {c: number of times c appears in stra}
    #   db = {c: number of times c appears in strb}
    #  return da == db
    pass

def main():
    assert is_anagrams("AB", "BA") == True
    assert is_anagrams("ABC", "BCA") == True
    assert is_anagrams("ABC", "BCD") == False

if __name__ == "__main__":
    main()