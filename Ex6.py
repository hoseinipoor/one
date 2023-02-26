# Write a Python function to calculate the factorial of a number
def factorial_func(number):
    if number == 0:
        return 1
    
    factorial_val =1
    for i in range(2,number+1):
        factorial_val *= i
    return factorial_val


number = int(input('Enter number: '))
while number<0 :
    number = int(input('number should be non negative ,Enter number again: '))

factorial_val=factorial_func(number)
print(f'factorial value is {factorial_val}')


