# Write a Python function to check whether a number falls within a given range
def check_func(number,down_rang,up_rang):

    return number>down_rang and number<up_rang
        

number = float(input('Enter number: '))
down_rang =  float(input('Enter down range: '))
up_rang =  float(input('Enter up range: '))

result=check_func(number,down_rang,up_rang)
print(result)

