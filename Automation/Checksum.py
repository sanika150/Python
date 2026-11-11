import hashlib

data = "Hello World"

hobj = hashlib.md5()
hobj1 = hashlib.sha256()

hobj.update(data.encode())
hobj1.update(data.encode())

checksum = hobj.hexdigest()
checksum1 = hobj1.hexdigest()

print("Checksum:", checksum)
print("Checksum1:", checksum1)