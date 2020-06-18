# 1.1 
# 
# Implement an algorithm to determine if a string has all unique characters
# What if you can not use additional data structures?

def isUnique(str):
    if not str:
        return False
    occurences = {}
    for letter in str:
        if occurences.get(letter):
            return False
        else:
            occurences[letter] = True
    return True

def isUniqueNoHash(str):
    # Empty string
    # None string
    if not str:
        return False
    for x in range(len(str)):
        for y in range(x + 1, len(str)):
            if str[x] == str[y]:
                return False
    return True


def main():
    print(isUnique("It is sunny"))
    print(isUnique("ABCDEF"))
    print(isUnique(""))
    print(isUnique(None))

    print(isUniqueNoHash("It is sunny"))
    print(isUniqueNoHash("ABCDEF"))
    print(isUniqueNoHash(""))
    print(isUniqueNoHash(None))

if __name__ == "__main__":
    main()
