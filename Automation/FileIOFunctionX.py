import os
def main():
	FileName = input("Enter the file name: ")

	if(os.path.exists(FileName)):
		fobj = open(FileName,"w")

		print(fobj.readable())
		print(fobj.writable())
		print(fobj.seekable())
		
	else:
		print("There is no such path")
if __name__ == "__main__":
	main()