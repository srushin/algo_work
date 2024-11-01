##Split in Half
##Given a string. Split it into two equal parts. Swap these parts and return the result.
##If the string has odd characters, the first part should be one character greater than the second part.
##Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

str_a = input('Please enter a string: ')
half_length = len(str_a) // 2
def split_arrange(str_a):
    if len(str_a) % 2 == 0:
        first_half = str_a[:half_length]
        second_half = str_a[half_length:]
        return second_half + first_half
    else:
        first_half = str_a[:half_length + 1]
        second_half = str_a[half_length + 1:]
        return second_half + first_half

print(f'{split_arrange(str_a)}')

##Unique Characters in String
##Given a string, determine if it consists of all unique characters.
##For example, the string 'abcde' has all unique characters and should return True.
##The string 'aabcde' contains duplicate characters and should return False.

str_1 = input('Please enter a string: ')
set_1 = {*str_1}

if len(str_1) == len(set_1):
    print(f'True')
else:
    print(f'False')
