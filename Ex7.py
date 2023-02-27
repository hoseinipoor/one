# Write a Python function that accepts a string and counts the number of upper and lower case letters
def count_upper_lower(input_string):
    up = 0
    low = 0
    for character in input_string:
        if character.isupper():
            up += 1
        elif character.islower():
            low += 1
    
    return up,low
    


input_string = input('Enter string: ')

up_count,low_count=count_upper_lower(input_string)

print(f'number of uppercase are {up_count} and lowercase are {low_count}')


