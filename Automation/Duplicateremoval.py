import hashlib
import os
import sys

def CalculateCheckSum(FileName):
	fobj = open(FileName,"rb")#binary mode

	hobj = hashlib.md5()
	buffer = fobj.read(1000) #it will read first 1KB
	while(len(buffer)>0):#check upto size greater than 0
		hobj.update(buffer)
		buffer = fobj.read(1000)

	fobj.close()
	return hobj.hexdigest()




def FindDuplicate(DirName = "Marvellous"):
	Ret = False
	Ret = os.path.exists(DirName)
	if Ret == False:
		print("There is no such directory")
		return

	Ret = os.path.isdir(DirName)
	if (Ret == False):
		print("It is not a directory")
		return
 
	Duplicate = {}

	for FolderName,SubFolderName,FileName in os.walk(DirName):
		for fname in FileName:
			fname = os.path.join(FolderName,fname)
			Checksum = CalculateCheckSum(fname)
			
			if Checksum in Duplicate:
				Duplicate[Checksum].append(fname)
			else:
				Duplicate[Checksum]=[fname]
	return Duplicate
		

def DeleteDuplicate(Path = "Marvellous"):
	MyDict = FindDuplicate(Path)
	Result = list(filter(lambda x : len(x)>1,MyDict.values()))

	Count = 0
	Cnt = 0

	for value in Result:
		for subvalue in value:
			Count = Count + 1
			if(Count > 1):
				print("Deleted file : ",subvalue)
				os.remove(subvalue)
				Cnt = Cnt + 1
		Count = 0

	print("Total deleted files : ",Cnt)

def main():
	if len(sys.argv) != 2:
		print("Invalid numbers of arguments")
		print("Please specify the name of directory")
		return

	DeleteDuplicate(sys.argv[1])
	



if __name__ == "__main__":
	main()