#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copyList = []
    if my_list:
        for i in range(len(my_list)):
            if my_list[i] == search:
                copyList.append(replace)
            else:
                copyList.append(my_list[i])
        return copyList
