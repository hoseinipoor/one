# Write a Python function that takes a list and 
# returns a new list with distinct elements from the first list.
def distinct_func(input_list):
    new_list = []
    for member in input_list:
        if member not in new_list:
            new_list.append(member)
    return new_list


N = int(input('How many members does the list have : '))
my_list = []
for i in range(N):
    num = int(input(f'Enter {i+1}th number:'))
    my_list.append(num)

result = distinct_func(my_list)
print(f'distinct list is {result}')


