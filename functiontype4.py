#Function type 4:
#Accept :Multiple parameter 
#Return :1 value
def Demo(Value1,Value2):
    print("Inside function",Value1,Value2)
    return Value1+Value2

def main():
    Result = Demo(10,20)
    print("Result is :",Result)


if __name__ == "__main__":
    main()