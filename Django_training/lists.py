#lists
mylist=[1,2,3]

mylist=[1,'two',3,False]

print(mylist)

#lenght of the list
print(len(mylist))

#pick an item
print(mylist[0])

#add new item
mylist.append("New Item")

print(mylist)

mylist.append(['x','y','z'])

print(mylist)

mylist.extend(['x','y','z'])

print(mylist)

item=mylist.pop()

print(item)

print(mylist)

item=mylist.pop(0) #adding indexes

print(item)
print(mylist)

mylist.reverse()

print(mylist)

mylist=[1,3,5,2]

mylist.sort()

print(mylist)

#nested lists
matrix=[[1,2,3],[4,5,6],[7,8,9]]

print(matrix[0][0])
print(matrix[1][2])

first_col = [row[0] for row in matrix]

print(first_col)