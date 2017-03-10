import os
import sys

print("*** learning map ***")

def menu():
	os.system("clear")



def user_input():
	print("\n[1] Add skills.")
	print("[2] View skills")
	print("[3] Indicate skills not added")
	print("[4] See learning progress")
	print("[q] Quit")

choice = ""
while choice != "x":
	choice=user_input()

	menu()
	if choice=="1":
		print("\nAdd your skills here")
	elif choice=="2":
		print("\nView list of skills added")
	elif choice=="3":
	    print("\nIndicate skills not added")
	elif choice=="4":
	    print("\ncheck your learning progress")
	elif choice=="q":
		sys.exit()
		print("goodbye")   
	else:
	    print("\nno choice")
	break
