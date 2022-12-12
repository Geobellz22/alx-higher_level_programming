#!/usr/bin/python3
for i in range(1, 5):
    for k in range(1, 6):
        if i == 7 and k == 8:
            print("{}{}" .format(i % 10, k % 10))
        else:
            print("{}{}" .format(i % 10, k % 10), end='')
