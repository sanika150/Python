def demo(a,b):
    if (a > b):
        print(a,"is greater")
    else:
        print(b,"is greater")



def  main():
    
    print("Enter first number:")
    No1 = int(input())
    print("Enter second number:")
    No2 = int(input())

    demo(No1,No2)

    

if __name__ == "__main__":
    main()