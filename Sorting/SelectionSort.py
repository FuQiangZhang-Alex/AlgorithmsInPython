

def select_max(lst):
    if not isinstance(lst, list):
        return None
    min_index = 0
    for index, item in enumerate(lst):
        if item < lst[min_index]:
            min_index = index
    return min_index


def select_sort(lst):
    if not isinstance(lst, list):
        return None
    for index, item in enumerate(lst):
        min_index = select_max(lst[index:])
        lst[min_index + index], lst[index] = lst[index], lst[min_index + index]
    return lst

arr = [3, 4, 1, 7, 0, 2, 11, 4, 8]
print(arr)
print(select_sort(arr))
