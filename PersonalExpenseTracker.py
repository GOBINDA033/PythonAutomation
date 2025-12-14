print("Welcome to personal expense tracker")
food=0.0
bills=0.0
rent=0.0
travel=0.0
transport=0.0
others=0.0
total_expense=0.0
while True:
    print("choose an option:")
    print("1.Add expense")
    print("2.View total expense")
    print("3.Exit")
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            print("Choose expense category:")
            print("1.Food\n2.bills\n3.rent\n4.travel\n5.transport\n6.others")
            category=(input("Enter your category choice:"))
            amount=float(input("Enter the expense amount $ "))
            if category=="food":
                food+=amount
            elif category=="bills":
                bills+=amount
            elif category=="rent":
                rent+=amount
            elif category=="travel":
                travel+=amount
            elif category=="transport":
                transport+=amount
            elif category=="others":
                others+=amount
            else:
                print("Invalid category choice")
        case 2:
                total_expense=food+bills+rent+travel+transport+others
                print("total expense amount: $",total_expense)
        case 3:
              print("Exting the expense tracker system.")
              break
        case _:
            print("Invalid choice please try again.")

            