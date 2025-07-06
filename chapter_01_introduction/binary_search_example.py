print("Binary Search Exemple")

def binary_search(list, item):
    low = 0

    # print("List length:", len(list)) # 5

    high = len(list) -  1 # 5 - 1 = 4 > Last item in the list

    # print("High: ", high) # 4

    while low <= high: # While we haven't reached the last item in the list
        mid = (low + high) // 2 # 0 + 4 / 2 = 2

        # print("Mid: ", mid) # 2, 0, 1

        guess = list[mid] # Get the middle element (our guess) 

        # print("Guess", list[mid]) # 5, 1, 3

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

cool_list = [1, 3, 5, 7, 9]

print("Found it! It's at index: ", binary_search(cool_list, 3))