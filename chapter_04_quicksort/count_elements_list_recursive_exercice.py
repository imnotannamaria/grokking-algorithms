def count_elements_list_recursive(list):
    if len(list) == 0:
        return 0
    else:
        return 1 + count_elements_list_recursive(list[1:])

print(count_elements_list_recursive([2, 2, 2, 2, 2, 2, 2]))