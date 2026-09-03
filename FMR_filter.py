#filter even number user input list
CheckEven = lambda No1: No1 % 2 == 0


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

if __name__ == "__main__":
    main()