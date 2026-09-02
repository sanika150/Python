'''List is ordered collection, 
 store multiple values of mixed type
 allows duplicate value
 we can modify(mutable)
 data store in inscript operator'[]'
'''
print("List")
data=[10,20,5.6,6,22,90]
print(data)
print(type(data))
print(len(data))
print(id(data)) #return unique identity
print(data[2])
#data[0]="abc"
#data[1]=3.5 #List allow duplicates
print(data)
print("-----------------------\n")

for i in range(4):
    print(data[i])

print("-----------------------\n")

sum = 0
for i in range(4):
    sum  = sum + data[i]

print("Summation is :",sum)
