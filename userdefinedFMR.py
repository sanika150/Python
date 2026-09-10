#filter even number user input list
#Map - increment filter data
CheckEven = lambda No: (No % 2 == 0)

Increment = lambda No: No+1

Add = lambda A,B:A+B

def filterx(Task,element):
  Result = list()

  for no in element:
    ret = Task(no)

    if ret == True:
      Result.append(no)

  return Result

def mapx(Task,element):
  Result = list()

  for no in element:
    ret = Task(no)
    
    Result.append(ret)

  return Result


def reducex(Task,element):
  sum = 0

  for no in element:
    sum = Task(sum,no)

  return sum

def main():
    size = int(input("Enter the size : "))
    value = 0

    data = list()
    for i in range(size):
        value = int(input())
        data.append(value)

    print("Actual data is : ",data)

    Fdata = list(filterx(CheckEven,data))
    print("Filtered data is : ",Fdata)

    Mdata = list(mapx(Increment,Fdata))
    print("Mapped data is : ",Mdata)

    RData =reducex(Add,Mdata)
    print("Data after reduce is :",RData)

if __name__ == "__main__":
    main()