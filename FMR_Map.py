#filter even number user input list
#Map - increment filter data
CheckEven = lambda No: No % 2 == 0

Increment = lambda No: No+1


def main():
    size = int(input("Enter the size : "))
    value = 0

    data = list()
    for i in range(size):
        value = int(input())
        data.append(value)

    print("Actual data is : ",data)

    Fdata = list(filter(CheckEven,data))
    print("Filtered data is : ",Fdata)

    Mdata = list(map(Increment,Fdata))
    print("Mapped data is : ",Mdata)

if __name__ == "__main__":
    main()