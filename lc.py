#Without List Comprehension

fruits = ["apple", "grape", "cherry", "kiwi", "bomboclat"] 
newlist = [] 
for x in fruits: 
 if "a" in x: 
  newlist.append(x) 
print(newlist)

#With List Comprehension

fruits = ["apple", "grape", "cherry", "kiwi", "bomboclat"] 
newlist = [x for x in fruits if "a" in x] 
print(newlist)