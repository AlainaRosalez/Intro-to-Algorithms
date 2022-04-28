#loop to continuously run the program
while(1):
    #input value
    num = int(input("Enter a number: "))

    #central function declaration
    def checkMod(divBy):
        #checks if the number is evenly divisible by the number it is checked against
        if(num % divBy == 0):
            print(f"{num} is divisible by {divBy}")
        else:
            print(f"{num} is not divisible by {divBy}")

    #calls the function 4 times with all 4 numbers that we wish to check against the input number
    checkMod(3)
    checkMod(4)
    checkMod(11)
    checkMod(17)