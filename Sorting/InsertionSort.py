

def insert_sort(lst):
    if not isinstance(lst, list):
        return None
    for index, item in enumerate(lst):
        if index == 0:
            continue
        for ind, it in enumerate(lst[:index]):
            if lst[index] < it:
                lst[index], lst[ind] = lst[ind], lst[index]
    return lst

arr = [3, 4, 1, 7, 0, 2, 11, 4, 8, 6]
print(insert_sort(arr))
