#checksum is use to check whether file is change, content of 2 files are same
#to verify files after downloading,detect duplicate files
#Checksum = A unique fingerprint of file contents.
"""
Statement	Purpose
import hashlib	Imports hashing module
hashlib.md5()	Creates MD5 hash object
data.encode()	Converts string into bytes
hobj.update()	Updates hash with data
hobj.hexdigest()	Returns checksum in hexadecimal
Python provides the built-in hashlib module.

It supports algorithms such as:
- MD5
- SHA1
- SHA256
- SHA512

Algorithm	Hash size	Security	Recommendation
MD5	128 bits	Weak	Avoid
SHA1	160 bits	Weak	Avoid
SHA256	256 bits	Strong	Recommended
SHA384	384 bits	Strong	Good
SHA512	512 bits	Strong	Good
SHA3-256	256 bits	Strong	Good
BLAKE2b	Up to 512 bits	Strong	Excellent
"""


import hashlib
def CalculateCheckSum(FileName):
	fobj = open(FileName,"rb")#binary mode useful because checksum calculations should operate on the exact file contents, including binary files

	hobj = hashlib.md5() #object of hashlib
 # store 1KB in buffer variable
 #Instead of loading the entire file into memory, we read it in smaller chunks.This is memory efficient for large files.
	buffer = fobj.read(1000) #it will read first 1KB
	while(len(buffer)>0):#check upto size greater than 0 
     #updating adding current chunk of data in md5 object
		hobj.update(buffer) #if size is < 0 empty or end of file 
		buffer = fobj.read(1000) #reads next 1000 bytes

	fobj.close()
    #hexdigest() converts the calculated MD5 hash into a hexadecimal string.
    #MD5 produces a 128-bit hash.
    #Its hexadecimal representation contains 32 characters.
	return hobj.hexdigest()



def main():
	Ret = CalculateCheckSum("Demo.txt")
	print("Checksum is ",Ret)




if __name__ == "__main__":
	main()