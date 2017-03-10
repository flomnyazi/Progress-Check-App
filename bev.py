def menu(list, question):
    for entry in list:
        print(1 + list.index(entry),)
        print(") " + entry)

    return input(question) - 1

#Give the computer some basic information about the list:

items =  ["1:TDD", "2:Virtual Environment", "3:Front End", "4:Html and CSS"]
complete = []

#Give some introductary text:
print("Welcome to andela Homelabs")

print("Go through the provided tasks and ensure completion before 4:30 pm")
print("the following are the list of tasks for today")
print(len(items), "tasks:")
for x in items:
    print(x)

completed =[]



print("These are your completed tasks:")

print (items[2])
completed=(items[2])

print ("This is your progress report")

for x in items:
	a=len(items)
	print (a/len(items)*100)
	






