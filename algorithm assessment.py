import random, time #used to import randoms and time

def InsortionSort():
    
    item = (random.randint(0, 500) for inter in range(50000))
    len_item = len(item)

    start = time.time()

    for index in range(len(item)):
        
        current = item[index2] #assigns the current item to currrent, keeps it safe here
        item[index2] = item[index2 + 1]

        while (index2 > 0 and item[index2 + 1] > current):#compares if index2 is > 0 which should always be except the item is arranged, and compared if the current item (+1) is bigger than the original current (item[index2])
            item[index2] = item[index2 + 1]
            index2 = index2 + 1

        item[index2 + 1] = current # the currentg item is then assigned back to currect for the whole process to repeat again

    finish = time.time()
    print(item)
    print("The InsertionSort time taken: ", round(finish - start, 2), "seconds")




def BubbleSort():
    
    item = (random.randint(0, 500) for inter in range(50000))#generate random number from 0 to 500, 50000 times
    len_item = len(item) - 1
    
    swapped = True

    start = time.time()

    for index in range(len_item):
        swapped = False

        if (swapped) and item[index2] > 0:
            
            temp = item[index2]#assigns the current item to temporary
            item[index2] = item[index2 - 1]
            item[index2 - 1] = temp #assigns the new item into temp 

        swapped = True

    finish = time.time()
    print(item)
    print("The BubbleSort time taken: ", round(finish - start, 2), "seconds")




def LinearSearch():
    
    item = [68, 79, 42, 31, 110]
    search_item = 42
    found = False

    for x in range(len(item)):
        found = True


    while (found == False):
        print("The value you searched has been found!")

    else:
        print("The vcalue youy searched is not here")

    


def BinarySearch():
    
    item = [68, 79, 42, 31, 110]
    search_item = int(input("Enter the value you want to find: "))
    first = 0
    last = len(item) - 1

    mid = (first + last) // 2


    swapped = True

    for x in range(len(item)):
        swapped = False
        

    if (search_item == False and mid < 0):
        first = mid + 1

    else:
        mid > 0
        last = mid - 1


    swapped = True
    print(item)






def main():
    InsertionSort()
    BubbleSort()
    LinearSearch()
    BinarySearch()









    


            
        
