#in lambda we can have any no of arguments
#lambda function for addition
Add = lambda No1,No2:No1+No2

#lambda function for check even
CheckEven = lambda No1: No1 % 2 == 0


def main():
    No1 = int(input("Enter first number :\n"))
    No2 = int(input("Enter second number :\n"))

    Ret = Add(No1,No2)
    print("Addition of two numbers are:",Ret)

    Ret1= False
    Ret1 = CheckEven(No1)
    if (Ret1 == True):
        print("It is Even")
    else:
        print("It is Odd")

if __name__ == "__main__":
    main()