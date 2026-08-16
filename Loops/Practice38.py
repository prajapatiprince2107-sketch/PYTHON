# word user se lena
word = input("Enter your word: ")
count = 0

for char in word:
    if char in "aeiou":
        count += 1

print(count)