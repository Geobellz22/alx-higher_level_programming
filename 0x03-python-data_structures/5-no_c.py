#!/usr/bin/python3
def no_c(my_string):
    for chr in my_string:
        if chr == 'c' and chr == 'C':
            continue
        else:
            new_string += chr
    return new_string
