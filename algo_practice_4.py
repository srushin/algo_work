#Even First
#Your input is a list of integers, and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input list).
#Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

def even_first(arr):
    next_even, next_odd = 0, len(arr)-1
    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            next_odd -= 1


test_arr = [7, 3, 5, 6, 4, 10, 3, 2] # should equal [6, 4, 10, 2, 7, 3, 5, 3]
even_first(test_arr)
print(test_arr)