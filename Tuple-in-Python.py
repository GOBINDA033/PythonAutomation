# The main concept the behind of the tuple:
#1 Tuple are orderd #2 Unchangable #3 it allows add to do duplicate values,

#How to create tuple
Student=("Gobinda","Ram","Jitender")

print(Student[0])
stu=("Gobinda",)

#How to update


Student1=list(Student)
Student1[0]="Rawat"

Student=tuple(Student1)
print(Student)

#Adding two tuple 
Student+=stu
print(Student)