
MINIMUM_LENGTH = 8

user_password = input("Please input password: ")
while len(user_password) < MINIMUM_LENGTH:
    print("Invalid password")
    user_password = input("Please input password: ")
for i in range(len(user_password)):
    print("*", end='')
print()
