import os
import sys

def DirectoryScanner(DirName="Marvellous"):
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
    Border = "-" * 50
    print(Border)
    print("-------------Automation Report---------")
    print("Total files scanned : ", FileCount)
    print("Total Empty Files count: ", EmptyFileCount)
    for file in EmptyFileList:
        print(file)
    print(Border)


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