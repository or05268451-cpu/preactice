        #BUBBLE SORT
# enter a list of data items
data = [25, 67, 8, 92, 50, 12, 9, 2]

n = len(data)-1
swapped = True

while (swapped) and n > 0:
    
    swapped = False
    
    for index in range(0, n):# use two definite for loops to make sure all the data are swapped and sorted

        if  (data[index] > data [index+1]):
                
            temp = data[index]# 25 which is data 0 is being assighned to  temporary
            data[index] = data[index+1]# data 1 "67" is then assigned to data 0 "25" # (0 then becomes 67)
            #both data 0 and data 1 is now "67"
            data[index+1] = temp # data 1 "67" is then assigned back to data 1 "temp = 25". that is data 1 becomes 25 while data 0 becomes 67
#(this is the swap)

            swapped = True

    n = n - 1

print(data)


