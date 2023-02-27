#Write a Python function to sum all the numbers in a list
#based on question,input is a list 
def sum_func(input_list):
    sum_value = 0
    for num in input_list:
        sum_value  += num 
    return sum_value


N = int(input('How many numbers should be sum: '))
numbers = []
for i in range(N):
    num = float(input(f'Enter {i+1}th number:'))
    numbers.append(num)

result = sum_func(numbers)
print(f'sum value is {result}')

