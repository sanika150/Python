import os
import sys

def DirectoryScanner(DirName="Practice"):
    Ret = False

    Ret = os.path.exists(DirName)

    if (Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName)
    if (Ret == False):
        print("its not a directory")
        return

    #print("Contents of the directory are : ")

    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:
            fname = os.path.join(FolderName, fname)
            print("FileName : ", fname)
            print("File size: ", os.path.getsize(fname))

def main():
	Border = "-"*50
	print(Border)
	print("-------DirectoryScannner---")
	print(Border)

	if(len(sys.argv)!=2):
		print("Invalid numbers of arguments")
		print("Please specify the name of directory")
		return

	

	DirectoryScanner(sys.argv[1])

if __name__ == "__main__":
	main()