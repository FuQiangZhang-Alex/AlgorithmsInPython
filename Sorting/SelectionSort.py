

def select_max(lst):
    if not isinstance(lst, list):
        return None
    max_index = 0
    for index, item in enumerate(lst):
        if item > lst[max_index]:
            max_index = index
    return max_index


def select_sort(lst):
    if not isinstance(lst, list):
        return None
    for index, item in enumerate(lst):
        max_index = select_max(lst[:len(lst) - index])
        lst[max_index], lst[len(lst) - index - 1] = lst[len(lst) - index - 1], lst[max_index]
    return lst

arr = [3, 4, 1, 7, 0, 2, 11, 4, 8]
print(arr)
print(select_sort(arr))
