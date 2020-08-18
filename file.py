import os
import copy

def main():
    for block in readNLines("./test.txt", 2):
      print(block)
    for i in range(90, 110):
      print(str(i).zfill(3))

def readNLines(filePath, N):
    fp = open(filePath)
    block = []
    count = 0
    while True:
        line = fp.readline()
        count = count + 1
        if not line:
            break
        block.append(line)
        if count == N:
            returnBlock = copy.deepcopy(block)
            block = []
            count = 0
            yield returnBlock
              
    if len(block) != 0:
      yield block  

if __name__ == '__main__':
  main()


