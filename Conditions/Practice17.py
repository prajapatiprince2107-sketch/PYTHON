# username correct
#       ↓
# password correct
#       ↓
# # Login Successful
username = (input("Enter username: "))
password = int(input("Enter password: "))

if username == "admin":
    if password == "1234":
       print("Login Successful")
    else:
        print("Wrong Username")
else:
    print("Wrong Password")