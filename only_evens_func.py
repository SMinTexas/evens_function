# Write a function that accepts a list of numbers as an argument.
# Return a new list that includes only the even numbers.
#
# only_evens([11, 20, 42, 97, 23, 10]) # Returns [20, 42, 10]
#
# Hint - use your is_even_func function to determine which numbers
#        to include in the new list
import is_even_func

numbers = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
evens = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)

print('')
print(f'Original List: {numbers}')
print('')
print(f'New List: {evens}')
print('')


