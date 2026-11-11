def main():
	try:
		fobj=open("Demo.txt","r")
		print("File gets successfully opened")
		
		print("Current offset is :",fobj.tell())
	#seek() method is used to change the current file position. It takes two parameters: offset and whence. The offset is the number of bytes to move, and whence specifies the reference point for the offset. The possible values for whence are:
	#0: Seek from the beginning of the file (default).
		fobj.seek(4,0)
		print("Current offset is :",fobj.tell())
		Data = fobj.read(6)
		print("Current offset is:",fobj.tell())

		print("Data from file is:",Data)
		fobj.close()
	except FileNotFoundError:
		print("Unable to open the file as there is no such file")
	finally:
		print("End of application")
		
if __name__ == "__main__":
	main()