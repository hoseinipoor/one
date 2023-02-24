#define function
def discount_calc(price,discount_percent):
    #calculate discount
    discount_value = price*discount_percent/100
    return discount_value

#get price
price = int(input('Enter price(toman): '))
while price<0 :
    price = int(input('price shouldn\'t be negative ,Enter price again: '))
    
#get discount_percent
discount_percent = int(input('Enter discount_percent(between 0 and 100): '))
while discount_percent<0 or discount_percent>100 :
    discount_percent = int(input('discount_percent should be between 0 and 100 ,Enter discount percent again: '))

#call function 
discount_value = discount_calc(price,discount_percent)
#print result 
print(f'discount value is {int(discount_value)} tomans')