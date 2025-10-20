#ask the user to input a number from 1 tp 100 in turn
for x in range(1, 101):
    response = input("Enter a number")

    if x % 3 == 0 and x % 5 == 0:
        if (response != "fizz_buzz"):
            print("Incorrect, the answer is fizz_buzz!")
        
    elif x % 3 == 0:
        if (response != "fizz!"):
            print("Incorrect, the answer is fizz!")
        

    elif x % 5 == 0:
        if (response != "buzz!"):
            print("Incorrect, the answer is buzz!")

    else:
        if (int(response) != x):
            print("Incorrect, the answer is ", x)
            

