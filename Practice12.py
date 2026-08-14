# 0–12   → Child
# 13–19  → Teenager
# 20–59  → Adult
# 60+    → Senior Citizen
age = int(input("Enter ur age: "))

if  age >= 0 and age <= 12:
    print("Child")
elif  age >= 13 and age <= 19:
    print("Teenager")
elif age >= 25 and age <= 59:
    print("Adult")
else:
    print("Senior Citizen")