#Function type 5:
#Accept :Multiple parameter 
#Return :Multiple value
def Demo(Value1,Value2):
    print("Inside function",Value1,Value2)
    return Value1+Value2

def main():
    Result = Demo(10,20)
    Result1 = Demo(20,30)
    Result2 = Demo(30,40)
    print("Result is :",Result,Result1,Result2)


if __name__ == "__main__":
    main()