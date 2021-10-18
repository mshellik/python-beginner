usr_string=input("Input your strig : ")
print(usr_string.title())
print("Do you want to conevert your string into Capital")
user_answer=input()
if user_answer=="yes":
    print(usr_string.upper())
else:
    print(usr_string.title())
