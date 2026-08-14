# Age >= 18
#    ↓
# Check whether age <= 60
#    ↓
# Eligible
age = int(input("Enter your age: "))

if age >= 18:
    if age <= 60:
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")