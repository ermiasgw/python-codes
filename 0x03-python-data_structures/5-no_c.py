#!/usr/bin/python3
def no_c(my_string):
    a = list(my_string)
    for i in a:
        if i == 'c':
            a.remove('c')
        elif i == 'C':
            a.remove('C')
    return str(a)
