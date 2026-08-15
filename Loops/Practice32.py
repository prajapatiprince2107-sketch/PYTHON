num = int(input("Enter your number: "))

count = 1
total = 0

while count <= num:
    total += count
    count += 1

print("Sum =", total)