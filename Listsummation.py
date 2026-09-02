def summation(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
    return sum

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

    Ret = 0 
    Ret = summation(Data)
    print("Summation is :",Ret)

if __name__ == "__main__":
    main()