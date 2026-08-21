'''
for getsizeof() return memory size
for that use below import 
from sys import getsizeof
'''

'''List is ordered collection, 
 store multiple values of mixed type
 allows duplicate value
 we can modify(mutable)
 data store in inscript operator'[]'
'''
print("List")
data=[10,20,"Python",3.5]
print(data)
print(type(data))
print(len(data))
print(id(data)) #return unique identity
print(data[2])
data[0]="abc"
data[1]=3.5 #List allow duplicates
print(data)
print("-----------------------\n")

'''
Tuple is ordered collection in indexing format
immutable cannot modify values
used for fixed data
data store in '()'
'''
print("Tuple")
a=(12,15,67)
print(a)
print(type(a))
print(len(a))
print(id(a))
print(a[2])
#a[3]=12 # error store only fixed data
#print(a)
#a[1]=45 # error cannot modify immutable
#print(a)
'''
Set unordered collection.
store unique values
mutable
use for removing duplicates
data enclosed in '{}'
'''
print("-----------------------\n")
print("Set")
s={1,2,3,4}
print(s)
print(type(s))
print(len(s))
print(id(s))
#s[5]=1 # no duplicates in set
#s[2]=45 # cannot assign object
print(s)

'''
range represent sequence of nos.
used in loops
range(start,step,stop)

'''
print("-----------------------\n")
print("Range")
r = range(1,5)
print(r)
print(type(r))
print(len(r))
print(id(r))

'''
Dictionary store key value pair data
key must be unique and immutable
values can be of any data type

'''
print("-----------------------\n")
print("Dictionary")
Data={"name":'ABC',"age":23}
print(Data)
print(type(Data))
print(len(Data))
print(id(Data))


'''
bytes immutable sequence
value range from 0 to 255
used in file handling and networking
'''
print("-----------------------\n")
print("bytes")
b = bytes([65,66,67])
print(b)
print(type(b))
print(len(b))
print(id(b))

'''
bytesarray mmutable sequence
value range from 0 to 255
can modify data
'''
print("-----------------------\n")
print("bytesarray")
ba = bytearray([65,66,67])
print(ba)
print(type(ba))
print(len(ba))
print(id(ba))
ba[0]=68
print(ba)

