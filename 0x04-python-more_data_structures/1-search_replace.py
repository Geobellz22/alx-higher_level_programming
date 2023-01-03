#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda: replace if x == search else x, my_list))
    return my_list
