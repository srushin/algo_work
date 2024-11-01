##Compute the sum of digits in all numbers from 1 to n.
##When a function gets a number n, find the sum of digits in all numbers from 1 to n.
##Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

number = int(input('Please enter a number: '))

result = number * (number+1)//2

print(f'The sum of all digits in your number is: {result}')


##Find the max number from 3 values.
##Example: 124, 21, 32. Result = 124.

number_a = int(input('Please enter a number: '))
number_b = int(input('Please enter a second number: '))
number_c = int(input('Please enter your final number: '))
def find_max(n1, n2, n3):
    if n1>n2 and n1>n3:
        return n1
    if n2>n1 and n2>n3:
        return n2
    return n3

big = find_max(number_a, number_b, number_c)

print(f'The largest number you entered is: {big}')

##Count odd and even numbers. Count odd and even digits of the whole number.
##Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

n = int(input('Please enter a number: '))
def count_oe(n):
    odds = []
    evens = []

    while n != 0:
        current = n % 10
        if current % 2:
            odds.append(current)
        else:
            evens.append(current)

        n = n // 10

    return ['Evens: ' +str(evens), 'Odds: ' +str(odds)]

print(count_oe(n))
