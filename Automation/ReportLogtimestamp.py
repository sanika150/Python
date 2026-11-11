import os
import sys
import time

def DirectoryScanner(DirName="Marvellous"):
    Border = "-" * 50
    timestamp = time.ctime()
    LogFileName = "Marvellous%s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")
    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write("This is a log file")
    fobj.write(Border+"\n")
 
    Ret = False

    Ret = os.path.exists(DirName)

    if (Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName)
    if (Ret == False):
        print("its not a directory")
        return

    FileCount = 0
    EmptyFileCount = 0
    EmptyFileList = []



    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:
            FileCount = FileCount + 1
            fname = os.path.join(FolderName, fname)
            print("FileName : ", fname)
            print("File size: ", os.path.getsize(fname))

            if os.path.getsize(fname) == 0:
                EmptyFileCount = EmptyFileCount + 1
                os.remove(fname)
                EmptyFileList.append(fname)
    
    
    fobj.write("Total files scanned : "+str(FileCount)+"\n")#int to string not possible

    fobj.write("Total Empty Files count: "+str(EmptyFileCount)+"\n")#+ for concatenation of string
    fobj.write(Border+"\n")
    for file in EmptyFileList:
        fobj.write(str(file)+"\n")

    fobj.write("This log file is created at : "+timestamp+"\n")
    fobj.close()


def main():
    Border = "-" * 50
    print(Border)
    print("-------DirectoryScannner---")
    print(Border)

    if len(sys.argv) != 2:
        print("Invalid numbers of arguments")
        print("Please specify the name of directory")
        return

    DirectoryScanner(sys.argv[1])

    print(Border)
    print("---------------------Directory Automation----------------")
    print(Border)


if __name__ == "__main__":
    main()