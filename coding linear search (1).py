import random

# create a list comprehension
lista = [random.randrange(1, 100) for x in range (1, 1000)]
found = False
count = 0

#ask a user to enter a search term
search_term = int(input("Enter a search item"))

# to create a loop to search through each data item in the list
for x in range(len(lista)):
    count += 1
    #compares the search_item to data item in the list
    if (search_term == lista[x]):
        found = True
        break
#using an if statement, check to see if found is true or false
if (found == True):
    print(f'Found data item! in {count}') # count tells how many times the number appears
else:
    print('Data item not found')
        

