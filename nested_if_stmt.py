# if statement for even number using function
def Result(a):
    if (a > 10):
        if(a< 30):
            print(a,"is between 10 and 30")
        else:
            print(a,"is equal to 10 or 30")



def  main():
    
    print("Enter the marks:")
    No = int(input())
    

    Result(No)

    

if __name__ == "__main__":
    main()