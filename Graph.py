import matplotlib .pyplot as plt
x=[5,6,7]
y =[11,12,13]
plt.plot(x,y)
plt.title("Bar line Graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show() 





#import matplotlib.pyplot as plt

# Data
students = ["Ram", "Shyam", "Mohan", "Ravi"]
marks = [85, 90, 78, 88]

# Bar graph
plt.bar(students, marks)

# Title aur labels
plt.title("Students Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

# Show graph
plt.show()
