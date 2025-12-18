def linearsearch():
    item = [11, 24, 6, 18, 94, 42]
    value = int(input("Enter the value you want to search for: "))

    found = False

    for x in range(len(item)):
        
        if (value == found):
            found = True

    if (value == True):
        print("The value searched is on the list!")
    else:
        print("The value searched is not on this list?")


def binarysearch():
    item = [6, 11, 18, 24, 42, 94]
    value = int(input("Enter the value you want to search for: "))

    first = 0
    last = len(item) - 1

    while(first <= last):
        mid = (first + last) // 2

        if (item[mid] == value):
            print("The value being searched is at index", mid)
            break

        elif (item[mid] < value):
            first = mid + 1

        else:
            last = mid - 1

    else:
        print("value not found!")


def bubblesort():
    item = [11, 24, 6, 18, 94, 42]
    
    n = len(item) 
    swapped = True

    while (swapped):
        swapped = False

        for index in range(0, n):

            if (item[index] > item[index + 1]):
                temp = item[index]
                item[index] = item[index + 1]
                item[index + 1] = temp

            swapped = True

    print(item)


def insertionsort():
    item = [11, 24, 6, 18, 94, 42]
    n = len(item) - 1

    for index in range(1, n):

        current = index
        index2 = index2 - 1

        while (index2 > 0 and item[index2 - 1] > current):

            item[index2] = item[index2 - 1]
            index2 = index2 - 1

        item[index2] = current

    print(item)
