# Here we are create list 
Language=["Java","Python","C Language","javaScript"]
Language2=["Go","Ruby","Swift"]
print(Language2)

#we can create list for different data types
mised_list=["Gobinda",22,True]
print(mised_list[0])

#inerting value in list
Language.insert(0,"HTML")
print(Language[0])

#appending of value in list
Language2.append("Kotlin")
print(Language2)

#extending list using for adding another list
Language.extend(Language2)
print(Language)

#removing value from list
Language.remove("C Language")
print(Language)

#popping using for removing last value
Language.pop(3)
print(Language)

#del using for deleting specification index value
del Language[1]
print(Language)

# clear using for removing all value from list
Language2.clear()
print(Language2)

#length using for count the list value
print(len(Language))

Language2.insert(0,"Java")
print(Language2)
Language.insert(1,"Rawat")
print(Language)
