# def count_sheep(n):
#     return ''.join(f"{i} sheep..." for i in range(1,n+1))

# def high_and_low(numbers):
#     x = max(list(numbers))
#     y = min(list(numbers))
#     return x + y


#test = ("8 3 -5 42 -1 0 0 -9 4 7 4 -4")

# def validate_pin(pin):
#     splt_pin = list(pin)
#     good_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#     new_pin = []
#
#     for x in splt_pin:
#         if x in good_numbers:
#             new_pin.append(x)
#     if len(new_pin) == 4 or len(new_pin) == 6:
#         return True
#     else:
#         return False
#
#
# test = ("1234")
#
# print(validate_pin(test))

test = 'Pig latin is cool'

# def pig_it(text):
#     words = text.split()
#     pig = []
#     for word in words:
#         if word.isalpha():
#             pig.append(word[1:] + word[0] + "ay")
#         else:
#             pig.append(word)
#     return " ".join(pig)
#
# print(pig_it(test))
#

def spin_words(sentence):
    words = sentence.split()
    new_words = []
    for x in words:
        if len(x) > 4:
            new_words.append(x[::-1])
        else:
            new_words.append(x)
    return " ".join(new_words)

print(spin_words(test))
