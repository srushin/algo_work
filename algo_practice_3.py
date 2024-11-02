#Below The Arithmetical Mean
#When given a list, the program should return a list of all the elements below the original list’s arithmetical mean. The arithmetical mean is the sum of all elements divided by the number of elements.
#Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

def below_mean(arr):
    arr_mean = sum(arr)/len(arr)
    less_mean = []
    for num in arr:
        if num < arr_mean:
            less_mean.append(num)
    return (less_mean)

test_arr = [1, 3, 5, 6, 4, 10, 2, 3]

print(below_mean(below_mean(test_arr)))


#Two Lowest Elements
#When given a list of elements, find the two lowest elements.
#They can be equal to each other or different.
#Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def low_elem(arr):
    sort_arr = sorted(arr)
    return sort_arr[0:2]

t_arr = [198, 3, 4, 9, 10, 9, 2, -1, -1]

print(low_elem(t_arr))


