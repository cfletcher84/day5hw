# Calculator App

# # num1 = int(input("What is your first number? : "))
# # num2 = int(input("What is your second number? : "))


def addition():
    num1 = int(input("What is your first number? : "))
    num2 = int(input("What is your second number? : "))
    total = num1 + num2
    print(f"Your total sum is {total}")

def subtraction():
    num1 = int(input("What is your first number? : "))
    num2 = int(input("What is your second number? : "))
    total = num1 - num2
    print(f"Your total difference is {total}")

def multiplication():
    num1 = int(input("What is your first number? : "))
    num2 = int(input("What is your second number? : "))
    total = num1 * num2
    print(f"Your procuct for this problem is {total}")

def divide():
    while True:
        try:
            num1 = int(input("What is your first number? : "))
            num2 = int(input("What is your second number? : "))
            total = num1 / num2    
            print(f"Your quotient for this problem is {total}")
            break
        except ZeroDivisionError:
            print("You cant divide by zero! Try again!")

def startApp():
    while True:
        user_input = (int(input("\nWhat opperation would you like?\n1. Addition\n2. Subtraction\n3. Multiplication\
                                \n4. Division\nPlease enter 1-4, 0 to quit: ")))
        if user_input == 0:
            break
        elif user_input == 1:
            addition()
            break
        elif user_input == 2:
            subtraction()
            break
        elif user_input == 3:
            multiplication()
            break
        else:
            divide()
            break

startApp()

# Shopping list

item_list = []

def list_add():
    while True:
        add_item = input("What would you like to add to your list? Nothing to quit : ")
        if add_item == "Nothing":
            break
        else: 
            item_list.append(add_item)
            print(f"You added {add_item} to your list!")

def list_remove():
    while True:
        try:
            remove_item = input("What item would you like to remove? Nothing to quit : ")
            if remove_item == "Nothing":
                break
            else:
                item_list.remove(remove_item)
                print(f"You removed {remove_item} from your list!")
        except ValueError:
            print(f"The item {remove_item} does not exist in the list!")

def print_list():
    print(f"\nHere is your curremt list of items: {item_list}.")
list_add()
list_remove()
print_list()

# Grade Analyzer

grades = [68,92,100,85,80,99,30,75,79,92,93,58,90]
grade_a =[]
grade_b = []
grade_c = []
grade_d = []
grade_f = []

def average_grade():
    total = sum(grades)
    average = total / len(grades)
    print(f"Your average is {average}.")
    return average

def highest_grade():
    grades.sort()
    print(f"The highest grade in the list is {grades[-1]}")

def lowest_grade():
    grades.sort()
    print(f"The lowest grade in the list is {grades[0]}")

def grade_letters():
    for grade in grades:
        if grade <=59:
            grade_f.append(grade)
        elif grade >= 60 and not grade > 69:
            grade_d.append(grade)
        elif grade >= 70 and not grade > 79:
            grade_c.append(grade)
        elif grade >= 80 and not grade > 89:
            grade_b.append(grade)
        else:
            grade_a.append(grade)
    print(f"The following grades are A's: {grade_a}\n\
        The following grades are B's: {grade_b}.\n\
        The following grades are C's: {grade_c}\n\
        The following grades are D's: {grade_d}\n\
        The following grades failed: {grade_f}")

average_grade()
highest_grade()
lowest_grade()
grade_letters()