
import datetime

def generateGCSFilePattern4(a, b):
    assert len(a) == len(b), "Input strings do not the same size"
    def patternGenerator(a, b):
        for i in range(0, len(a)):
            if (a[i] == b[i]):
                yield a[i]
            else:
                yield "[{}{}]".format(a[i], b[i])
    return str().join([c for c in patternGenerator(a, b)])

def main():
    print(generateGCSFilePattern4("20180131", "20180201"))

if __name__ == '__main__':
  main()