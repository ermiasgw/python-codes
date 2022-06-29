#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) not in 'qa':
        print("{0}".format(chr(i)), end="")
    else:
        continue
