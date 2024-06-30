#    Password
import random
import string

truechoice = ""
len = int(input("Enter password len: "))
while True:
    choice = input("Enter what string you want a-upper, b-lower, c-number, d-punctuation (enter 'stop' to end choice): ")
    if choice == "stop":
        break
    else:
        if choice == "a":
            truechoice += string.ascii_uppercase
        elif choice == "b":
            truechoice += string.ascii_lowercase
        elif choice == "c":
            truechoice += string.digits
        elif choice == "d":
            truechoice += string.punctuation
        else:
            print("Invalid choice, please enter a, b, c, d, or stop.")
userPass = ""
for i in range(len):
    userPass += random.choice(truechoice)
print(userPass)

#    Game
secret_number = random.randint(1, 100)
att = 0
while True:
    user_number = int(input("Enter number from 1-100(5 attemps): "))
    att += 1
    if att>5:
        print("You loose you attemps are more then 5")
        break
    elif user_number < secret_number:
        print("Number is higher")
    elif user_number > secret_number:
        print("Number is lower")
    else:
        print(f"You win secret number is {secret_number} you try {att} time")
        break