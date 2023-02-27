#Write a Python program to reverse a string
def reverse_func(input_string):
    L = len(input_string)
    new_string = ''
    for i in range(L):
        new_string = new_string + input_string[-(i+1)]
    
    return new_string


input_string = input('Enter string: ')
result_string=reverse_func(input_string)
print(f'result string is {result_string}')


