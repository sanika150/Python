def main():
	try:
		fobj=open("Demo.txt","w")
		print("File gets successfully opened")
		fobj.write("Jay Ganesh")
		fobj.close()
	except FileNotFoundError:
		print("Unable to open the file as there is no such file")
	finally:
		print("End of application")
		fobj.close()
if __name__ == "__main__":
	main()