
def Percentage(Marks, totalMarks):

	percentage = 0
	if(Marks > totalMarks or Marks < 0 or totalMarks < 0):
		print("Invalid input \n")
		return percentage
	
	percentage = (Marks / totalMarks)*100
	return percentage
	


def main():

	Value1 = 0
	Value2 = 0
	res = 0
	print("Enter the Marks: ")
	Value1 = int(input())
	print("Enter the total marks: ")
	Value2 = int(input())

	res = Percentage(Value1,Value2)

	print("Percentage is : ",res)



if __name__ =="__main__":
    main()
