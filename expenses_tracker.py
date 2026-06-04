import csv

FILE_NAME = "expenses.csv"

def add_expense():
    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("Expense Added Successfully!")

def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)           

            print("\nExpenses:")
            for row in reader:
                print(row)

    except FileNotFoundError:
        print("No expenses found!")

def total_expense():
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader, None)

            for row in reader:
                if len(row) >= 3:
                     total += float(row[2])
                     
        print("Total Expense =", total)

    except FileNotFoundError:
        print("No expenses found!")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")