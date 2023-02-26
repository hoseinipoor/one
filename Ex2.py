# Write a Python function to find the maximum of three numbers
def find_max(a,b,c):
    if a>b :
        if a>c :
            return a
        else : #a<=c
            return c
    else : # a<=b
        if b>c :
            return b
        else: # b<=c
            return c
num1 = float(input('Enter number1: '))
num2 = float(input('Enter number2: '))
num3 = float(input('Enter number3: '))

max_value  = find_max(num1,num2,num3) 
print(f'maximum value is {max_value}')
        
