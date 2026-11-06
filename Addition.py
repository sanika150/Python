def Addition(No1,No2):

	ans = 0
	ans = No1 + No2
	return ans


def main():
    

	Value1 = 0
	Value2 = 0

	res = 0
	print("Enter the first number: \n");
	Value1 = int(input())
	print("Enter the Second number: \n");
	Value2 = int(input())

	res = Addition(Value1,Value2);
	print("Result is : ",res)


if __name__ == "__main__":
    main()
