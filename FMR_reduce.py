from functools import reduce
#filter even number user input list
#reduce the data
CheckEven = lambda No: No % 2 == 0

Increment = lambda No: No+1

Add = lambda A,B : A+B


def main():
    size = int(input("Enter the size : "))
    value = 0

    data = list()
    for i in range(size):
        value = int(input())
        data.append(value)

    print("Actual data is : ",data)

    Fdata = list(filter(CheckEven,data))  #Typecast as list because we need data in list format
    print("Filtered data is : ",Fdata)

    Mdata = list(map(Increment,Fdata))  #Typecast as list because we need data in list format
    print("Mapped data is : ",Mdata)

    Rdata = reduce(Add,Mdata)
    print("Reduced data is : ",Rdata)

if __name__ == "__main__":
    main()