''' 1.Insert order does'nt preserved
2.Duplicated are not allowed
3.Hetrogeneous data types are allowed
4.It is mutable
5.slicing and indexing concept are allowed'''

s={1,2,3,4}
print(s)
l=[5,6,7,8]
l1=[11,23,45]

s.add(10) # add the element
s.update(l) # add the grp of element
print(s)

s.update(l1,range(5))
print(s)

s.remove(10) # if the number 10 is not available it will show error
s.discard(20) #it will remove whether the num is present or not

s.pop() # pop the value from the first index
print(s)

x={1,2,3}
y={3,4,5}

print(x.union(y)) #1,2,3,4,5

print(x.intersection(y)) # 3 same value occur in the both

print(x.difference(y)) # unique value occurs in x

print(x.symmetric_difference(y)) # unique value occurs in x and y
