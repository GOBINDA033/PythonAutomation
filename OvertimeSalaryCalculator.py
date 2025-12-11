 # 1.No I'm goin to create an OvertimeSalaryCalculator
rate=500
OvertimeRate=700
hoursWorked=float(input("Enter the number of hours worked:"))
if hoursWorked>8:
    overtimeHours=hoursWorked-8
    OvertimeSalary=overtimeHours*OvertimeRate
    print("Overtime Salary is:",OvertimeSalary)
else:
    regularSalary=hoursWorked*rate
    print("Regular Salary is:",regularSalary)


    #ExpenseCalculator

income=int(input("Enter your income:"))
houseRent=int(input("Enter your house rent expense:"))
foodExpense=int(input("Enter your food expense:"))
electricityBill=int(input("Enter your electricity bill expense:"))
TotalExpense=houseRent+foodExpense+electricityBill
print("Your total expense is:",TotalExpense)
if income>TotalExpense:
    savings=income-TotalExpense
    print("Your saving are :",savings)
elif income==TotalExpense:
    print("You have no savings.")
else:   
     deficit=TotalExpense-income
     print("You are in deficit of:",deficit)