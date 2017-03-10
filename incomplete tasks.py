def menu(list, question):
    for entry in list:
        print(1 + list.index(entry),)
        print(") " + entry)

    return input(question) - 1

#Give the computer some basic information about the list:

items =  ["1:TDD", "2:Virtual Environment", "3:Front End", "4:Html and CSS"]
incomplete = []

#Give some introductary text:
print("Welcome to andela Homelabs")

print("Go through the provided tasks and ensure completion before 4:30 pm")
print("the following are the list of tasks for today")
print(len(items), "tasks:")
for x in items:
    print(x)

incomplete =[]


print("These are your incomplete tasks:")

print (items[1])