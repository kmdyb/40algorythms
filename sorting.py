# algorytmy sortowania z książki
# bąbelkowe (bubble), wstawianie (insertion), scalanie (merge), Shell, wymiana (selection)
# TODO: złożoność obliczeniowa dla każdego algorytmu

# bubble sort
def bubble_sort(my_list):
    last_element_index = len(my_list) - 1
    for passNo in range(last_element_index, 0, -1):
        for idx in range(passNo):
            if my_list[idx] > my_list[idx + 1]:
                my_list[idx], my_list[idx + 1] = my_list[idx + 1], my_list[idx]
    return my_list


# insertion
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        j = i - 1
        element_next = my_list[i]
        while (my_list[j] > element_next) and (j >= 0):
            my_list[j + 1] = my_list[j]
            j = j - 1
        my_list[j + 1] = element_next
    return my_list


# merge sort
def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0

        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                my_list[k] = left[i]
                i += 1
            else:
                my_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1


# Shell
def shell_sort(my_list):
    distance = len(my_list) // 2
    while distance > 0:
        for i in range(distance, len(my_list)):
            temp = my_list[i]
            j = i
            # sortowanie do wyznaczonej granicy
            while j >= distance and my_list[j - distance] > temp:
                my_list[j] = my_list[j - distance]
                j = j - distance
            my_list[j] = temp
        # zmniejszenie granicy
        distance = distance // 2
    return my_list


# selection
def selection_sort(my_list):
    for fill_slot in range(len(my_list) - 1, 0, -1):
        max_index = 0
        for location in range(1, fill_slot + 1):
            if my_list[location] > my_list[max_index]:
                max_index = location
        my_list[fill_slot], my_list[max_index] = my_list[max_index], my_list[fill_slot]
