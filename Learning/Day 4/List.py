'''
1. Maintains insertion order
2. list is mutable we acn modify the elements
3. It allows the Hetrogenous data types
4.It allows the duplicates
5. we can access from index
6. Slicing also allodes
'''


list=[1,2,3,4,5,6,7,8]

print(list[0])

print(len(list)) # it returns the length of the list

list.append(9)
print( list) # it adds the element at the last

list.insert(0,10)
print(list) #we can add the element at the particular index

list.index(10)
print(list.index(9) )# it retrives the index of the given number)

print(list.count(1))  #it count how many times the present in the list

list.remove(2) #it removes the 2 from the list but it remove first 2 present in the list
print(list)

list.pop() # it removes th elast elemnt of the list

list.reverse() #it print the list in reverse

list.sort() # it sort the list for asce -> desc
list.sort(reverse=True) # Desc-> asec

print(list)

x=[1,2,3,4,5]
y=[6,7,8,9]

print(x+y)

print(x*3)

print(3 in y)

print(6 in y)

# nested list

newList=[[1,2,3],[4,5,6],[7,8,9]]

for i in newList:
    print(i)

for i in range(len(newList)):
    for j in range(len(newList[i])):
        print(newList[i][j],end=" ")
    print()

print(min(list))

print(max(list))
