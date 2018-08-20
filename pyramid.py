# -*- coding: UTF-8 -*-

for x in range(1, 8, 2):
    print '@' * x
    if x == 7:
        for x in range(5, 0, -2):
            print '@' * x
