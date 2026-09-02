# input function
#created addition function
#typecasting used for converting in integer

def Addition(Value1,Value2):
    Result =0
    Result = Value1 + Value2
    return Result


def main():
    print("Enter first number")
    No1 = int(input())

    print("Enter second number")
    No2 = int(input())

    Ans = Addition(No1,No2)

    print("Addition of two numbers is :",Ans)

if __name__ == "__main__":
    main()

   

    