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




def FindDuplicate(DirName="Marvellous"):
    Border = "-" * 50
    print(Border)

    if not os.path.exists(DirName):
        print("There is no such directory")
        return

    if not os.path.isdir(DirName):
        print("It is not a directory")
        return

    Duplicate = {}
    FileCount = 0
    EmptyFileCount = 0
    EmptyFileList = []

    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:
            FileCount += 1
            fname = os.path.join(FolderName, fname)
            print(Border)
            print("FileName : ", fname)
            print("File size: ", os.path.getsize(fname))

            if os.path.getsize(fname) == 0:
                EmptyFileCount += 1
                EmptyFileList.append(fname)

            

            Checksum = CalculateCheckSum(fname)

            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]

    print(Border)
    print("Total files scanned : ", FileCount)
    print("Total Empty Files count: ", EmptyFileCount)
    print(Border)
    print("Empty files are:")
    for file in EmptyFileList:
        print(file)

    #print("Empty files are :", EmptyFileList)
    return Duplicate


def DeleteDuplicate(Path = "Marvellous"):
    Border = "-" * 50
    MyDict = FindDuplicate(Path)
    Result = list(filter(lambda x : len(x)>1,MyDict.values()))

    Count = 0
    Cnt = 0
    print(Border)
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