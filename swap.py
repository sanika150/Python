


def main():

	Value1 = 0
	Value2 = 0
	Value3 = 0
 
	print("Enter first number: \n")
	Value1 = int(input())
	print("Enter second number: \n")
	Value2 = int(input())
	print("Before Swapping :",Value1,Value2)
 
	Value3 = Value1
	Value1 = Value2
	Value2 = Value3
 
	print("After Swapping :",Value1,Value2)
 
 
if __name__ == "__main__":
    main()