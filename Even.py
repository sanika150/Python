
def Even(No1):
	if No1 % 2 == 0:
		return True
	else:
		return False
	

def main():
    Value1 = 0
    res = False
    print("Enter the first number from user: \n")
    Value1 = int(input())
	

    res = Even(Value1)
    
    if res == True:
        print("Even number")
    else:
        print("Odd number")

    
	



if __name__ == "__main__":
    main()