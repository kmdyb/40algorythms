# algorytmy wyszukiwania z książki
# liniowy
# binarny
# interpolacyjny

def linear_search(my_list, item):
    index = 0
    found = False

    while index < len(my_list) and found is False:
        if my_list[index] == item:
            found = True
        else:
            index = index + 1
    return found


def binary_search(my_list, item):
    first = 0
    last = len(my_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if my_list[midpoint] == item:
            found = True
        else:
            if item < my_list[midpoint]:
                last = midpoint
            else:
                first = midpoint + 1
    return found


def int_search(my_list, x):
    idx0 = 0
    idxn = len(my_list) - 1
    found = False
    while idx0 <= idxn and my_list[idx0] <= x <= my_list[idxn]:
        mid = idx0 + ((float(idxn - idx0) / (my_list[idxn] - my_list[idx0])) * (x - my_list[idx0]))
        if my_list[mid] == x:
            found = True
            return True
        if my_list[mid] < x:
            idx0 = mid + 1
    return found
