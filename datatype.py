import sys

def main():
    

	a = 10
	ch ='Sanika'
	f = 21.5
	data = [10,20,'sanika']
	b = (10,20,30)
	r = range(1,5)
	s={10,20,30}
	
	
	print("value of integer is : ",a)
	print("value of character is : ",ch)
	print("value of float is : ",f)
	print("value of list is :",data)
	print("value of tuple is :",b)
	print("value of range is :",r)
	print("value of set is :",s)
 
	print("----------------------------------")
 
	print(type(data))
	print(type(b))
	print(type(r))
	print(type(s))

	print("----------------------------------")
	print("Address of a is: ",id(a))
	print("Address of ch is: ",id(ch))
	print("Address of f is: ",id(f))
	print("Address of list is: ",id(data))
	print("Address of tuple is: ",id(b))
	print("Address of range is: ",id(r))
	print("Address of set is: ",id(s))
	print("----------------------------------")
	print("Size of a is : ",sys.getsizeof(a))
	print("Size of ch is : ",sys.getsizeof(ch))
	print("Size of f is : ",sys.getsizeof(f))
	print("Size of list is : ",sys.getsizeof(data))
	print("Size of tuple is : ",sys.getsizeof(b))
	print("Size of range is : ",sys.getsizeof(r))
	print("Size of set is : ",sys.getsizeof(s))

	return 0


if __name__ == "__main__":
    main()