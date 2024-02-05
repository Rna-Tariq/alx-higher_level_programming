#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        for i in range(x):
            element = my_list[i]
            print(element, end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()
    return count
