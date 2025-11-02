def toBinary(number):           #(calling the function to input a number)
    remainders = []              #(an empty list)

    while number > 0:           #(keep dividing until number is 0)
        remainder = number % 2  #(%used to find a remainder)
        remainders.append(remainder)
        number = number // 2    #(to divide and keep the whole number)

    remainders.reverse()        #(flip the order)

    # (combine bits into one string)
    binary_string = "".join(str(bit) for bit in remainders)
    return binary_string        #(give the result back)


def main():
    number = int(input("Enter a number between 1 and 255: "))

    while number < 1 or number > 255:
        number = int(input("Invalid! Enter a number between 1 and 255: "))

    binary_value = toBinary(number)
    print("The binary value of", number, "is", binary_value)


main()
