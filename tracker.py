from datetime import date

if __name__ == '__main__':
    print('welcome to hana\'s homework tracker!')

    response = input('enter the due date for this homework assignment (yyyy mm dd): ')
    result = response.split()
    due = date(int(result[0]), int(result[1]), int(result[2]))

    homework = []

    while True:
        print("\nMenu")
        print("1. Add homework")
        print("2. View homework")
        print("3. Mark homework as done")
        print("4. Delete homework")
        print("5. Exit")

        choice = input("Pick a number: ")

        if choice == "1":
            name = input("Enter homework name: ")
            due = input("Enter due date like this: 2025 05 30: ")

            parts = due.split()
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])

            assignment = [name, date(year, month, day), False]
            homework.append(assignment)

            print("Homework added.")

        elif choice == "2":
            if len(homework) == 0:
                print("You do not have any homework yet.")
            else:
                for i in range(len(homework)):
                    print("\n" + str(i + 1) + ". " + homework[i][0])
                    print("Due:", homework[i][1])

                    if homework[i][2] == True:
                        print("Status: done")
                    else:
                        print("Status: not done")

                        if homework[i][1] < date.today():
                            print("This homework is overdue.")
                        elif homework[i][1] == date.today():
                            print("This homework is due today.")
                        else:
                            print("This homework is coming up.")

        elif choice == "3":
            if len(homework) == 0:
                print("There is no homework to mark.")
            else:
                for i in range(len(homework)):
                    print(str(i + 1) + ". " + homework[i][0])

                number = int(input("Which homework is done? "))

                if number >= 1 and number <= len(homework):
                    homework[number - 1][2] = True
                    print("Marked as done.")
                else:
                    print("That number is not on the list.")

        elif choice == "4":
            if len(homework) == 0:
                print("There is no homework to delete.")
            else:
                for i in range(len(homework)):
                    print(str(i + 1) + ". " + homework[i][0])

                number = int(input("Which homework do you want to delete? "))

                if number >= 1 and number <= len(homework):
                    homework.pop(number - 1)
                    print("Homework deleted.")
                else:
                    print("That number is not on the list.")

        elif choice == "5":
            print("Goodbye.")
            break

        else:
            print("Please pick a number from 1 to 5.")
