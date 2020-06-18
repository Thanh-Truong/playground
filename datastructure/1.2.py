# Write code to reverse a C-Style String (C-String means that “abcd” is represented as five characters, including the null character )
def reserve(str):
    return "".join([ str[x] for x in range(len(str)-1, -1, -1)])

def main():
    print(reserve("ABCD"))

if __name__ == "__main__":
    main()
