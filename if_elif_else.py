# if statement for even number using function
def Result(a):
    if (a >= 90):
        print("Grade A")
    elif(a >= 75):
        print("Grade B")
    elif(a >= 60):
        print("Grade C")
    else:
        print("Fail")



def  main():
    
    print("Enter the marks:")
    No = int(input())
    

    Result(No)

    

if __name__ == "__main__":
    main()3