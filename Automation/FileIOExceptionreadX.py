def main():
	try:
		fobj=open("Demo.txt","r")
		print("File gets successfully opened")
		
		Data = fobj.read(6)

		print("Data from file is:",Data)
		fobj.close()
	except FileNotFoundError:
		print("Unable to open the file as there is no such file")
	finally:
		print("End of application")
		fobj.close()
if __name__ == "__main__":
	main()