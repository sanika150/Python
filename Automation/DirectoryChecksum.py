import hashlib
import os
def CalculateCheckSum(FileName):
	fobj = open(FileName,"rb")#binary mode

	hobj = hashlib.md5()
	buffer = fobj.read(1000) #it will read first 1KB
	while(len(buffer)>0):#check upto size greater than 0
		hobj.update(buffer)
		buffer = fobj.read(1000)

	fobj.close()
	return hobj.hexdigest()



def DirectoryWatcher(DirName = "Marvellous"):
	Ret = False
	Ret = os.path.exists(DirName)
	if Ret == False:
		print("There is no such directory")
		return

	Ret = os.path.isdir(DirName)
	if (Ret == False):
		print("It is not a directory")
		return

	for FolderName,SubFolderName,FileName in os.walk(DirName):
		for fname in FileName:
			fname = os.path.join(FolderName,fname)
			Checksum = CalculateCheckSum(fname)
			print(f"File name: {fname} CheckSum :{Checksum}")
def main():
	DirectoryWatcher()




if __name__ == "__main__":
	main()
 
 
 """
 for FolderName,SubFolderName,FileName in os.walk(DirName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)


1.os.walk() is a function from Python's os module.

It is used to traverse a directory and all its subdirectories.

It returns three values:
Variable	Meaning
FolderName	Current directory path
SubFolderName	List of subdirectory names
FileName	List of filenames in the current directory

For example, suppose your folder structure is:
Marvellous

 Demo.txt

 test.py

 Python

 data.txt

 report.pdf



1.os.walk() is a function from Python's os module.

It is used to traverse a directory and all its subdirectories.

It returns three values:
Variable	Meaning
FolderName	Current directory path
SubFolderName	List of subdirectory names
FileName	List of filenames in the current directory

For example, suppose your folder structure is:
Marvellous

 Demo.txt

 test.py

 Python

 data.txt

 report.pdf

This is an inner loop.
- FileName contains a list of files.
- The loop processes one filename at a time.
- fname stores the current filename.
For example:
FileName = ["Demo.txt", "test.py"]for fname in FileName:    print(fname)


Step 3: os.path.join()
fname = os.path.join(FolderName, fname)



This combines the directory path and filename to create a complete file path.

For example:
FolderName = "Marvellous"fname = "Demo.txt"fname = os.path.join(FolderName, fname)print(fname)


"""