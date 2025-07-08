def sum_recursive(list):
    if len(list) == 0:
        return 0   
    else:
        return list[0] + sum_recursive(list[1:])


print(sum_recursive([2, 3, 6]))

