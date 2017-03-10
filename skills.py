#the menu function:
#the menu function:
def menu(list, question):
    for entry in list:
        print(1 + list.index(entry),)
        print(") " + entry)

    return input(question) - 1

#Give the computer some basic information about the room:
items = ["TDD","Virtual Environment","Front End","Html and CSS"]

#The key is in the vase (or entry number 2 in the list above):
keylocation = input()

#You haven't found the key:
keyfound = 0

loop = 1

#Give some introductary text:
print("Welcome to andela Homelabs")

print("Go through the provided tasks and ensure completion before 4:30 pm")
print("the following are the list of tasks for today")
print(len(items), "tasks:")
for x in items:
    print(x)
print("These are you completed tasks")


#Get your menu working, and the program running until you find the key:
while loop == 1:
    choice = menu(items,"completed tasks")
    if choice == 0:
        if choice == keylocation:
            print("You have already completed TDD")

            print("")
            keyfound = 1
        else:
            print("You have not completed the TDD.")
            print("")
    elif choice == 1:
        if choice == keylocation:
            print("You have completed Virtual Environment.")
            print("")

            keyfound = 1
        else:
            print("You have not completed virtual environment.")
            print("")
    elif choice == 2:
        if choice == keylocation:
            print("You have completed front end.")
            print("")
            keyfound = 1
        else:
            print("You have not completed front end")

            print("")
    elif choice == 2:
        if choice == keylocation:
            print("You have completed HTNL and CSS.")
            print("")
            keyfound = 1
        else:
            print("You have not completed HTML and CSS")

            print("")