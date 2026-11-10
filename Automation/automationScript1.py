import sys

def main():
	Border = "-" * 40
	print(Border)
	print("Automation project")
	print(Border)

	if len(sys.argv) == 2:
		if (sys.argv[1] == "--h") or (sys.argv[1] == "--H"):
			print("This application is used to perform----")
			print("This is automation script")
		elif (sys.argv[1] == "--u") or (sys.argv[1] == "--U"):
			print("Use the script as")
			print("ScriptName.py Argument1 Argument2")
			print("Argumrnt1:________")
			print("Argument2:________")
		else:
			print("Use the given flags:")
			print("--u: used to display the usage")
			print("--h: used to display help")
	else:
		print("Invalid number of arguments")
		print("--u: used to display the usage")
		print("--h: used to display help")

	print(Border)
	print("Thanks you for using script")
	print(Border)


if __name__ == "__main__":
	main()