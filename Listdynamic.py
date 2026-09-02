def main():
    size = 0
    value = 0

    print("Enter the number of element:")
    size = int(input())

    #create a list
    Data = list()
    
    print("Enter the element:")
    for i in range(size):
        value = int(input())
        Data.append(value)

    print(Data)

if __name__ == "__main__":
    main()