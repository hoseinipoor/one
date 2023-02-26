#Write a Python function to multiply all the numbers in a list
#based on question,input is a list 
def multiply_func(input_list):
    multiply_value = 1
    for num in input_list:
        multiply_value  *= num 
    return multiply_value


N = int(input('How many numbers should be multipled: '))
numbers = []
for i in range(N):
    num = float(input(f'Enter {i+1}th number:'))
    numbers.append(num)

result = multiply_func(numbers)
print(f'multiply value is {result}')


