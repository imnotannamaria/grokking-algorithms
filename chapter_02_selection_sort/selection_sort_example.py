def find_smallest(arr):
    min = arr[0]

    min_index = 0

    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_index = i

        return min_index

def selection_sort(arr):
    new_arr = []

    for i in range(len(arr)):
        min = find_smallest(arr)
        new_arr.append(arr.pop(min))

        return new_arr

print(selection_sort([5, 3, 6, 2, 10]))