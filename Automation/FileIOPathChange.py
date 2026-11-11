import os
def main():
	FileName = input("Enter the file name: ")

	Ret = os.path.isabs(FileName)
	if(Ret == True):
		fobj = open(FileName,"r")
		print("It is absolute path")
	else:
		print("It is relative path")
		NewPath = os.path.abspath(FileName)
		print("Updated Path: ",NewPath)
		
if __name__ == "__main__":
	main()