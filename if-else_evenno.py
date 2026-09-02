# if statement for even number using function
def Even(a):
    if (a % 2 ==0):
        print(a,"is even ")
    else:
        print(a,"is odd")



def  main():
    
    print("Enter the number:")
    No1 = int(input())
    

    Even(No1)

    

if __name__ == "__main__":
    main()