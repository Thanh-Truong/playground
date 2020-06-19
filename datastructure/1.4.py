from merge_sort import merge_sort
#Write a method to decide if two strings are anagrams or not
# Solution 1. return sort(stra) == sort(strb)
def is_anagrams_0(stra, strb):
    # this merge_sort implementation works only with array
    list_a = list(stra)
    list_b = list(strb)
    return merge_sort(list_a) == merge_sort(list_b)

# Solution 2. a number of occurence of every character in stra is the same in strb
#   da = {c: number of times c appears in stra}
#   db = {c: number of times c appears in strb}
#  return da == db
def is_anagrams_1(stra, strb):
    def count_occurences(str):
        d = {}
        for c in str:
            if d.get(c):
                d[c] = d[c] + 1
            else:
                d[c] = 1
        return d
    
    d_stra = count_occurences(stra)
    d_strb = count_occurences(strb)
    return d_stra == d_strb
    

def main():
    assert is_anagrams_0("AB", "BA") == True
    assert is_anagrams_0("ABC", "BCA") == True
    assert is_anagrams_0("ABC", "BCD") == False
    assert is_anagrams_1("AB", "BA") == True
    assert is_anagrams_1("ABC", "BCA") == True
    assert is_anagrams_1("ABC", "BCD") == False

if __name__ == "__main__":
    main()