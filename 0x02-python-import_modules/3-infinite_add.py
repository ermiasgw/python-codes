#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print(0)
    else:
        print(sum(list(map(int, sys.argv[1:]))))
