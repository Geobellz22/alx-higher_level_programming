#!/usr/bin/python3
def max_integer(my_list=[]):
    for i in range (len(my_list)):
        if len(my_list) == 0:
            return None, 0
        else:
            return len(my_list), my_list[0]
