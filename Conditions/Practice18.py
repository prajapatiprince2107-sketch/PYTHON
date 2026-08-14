# marks >= 0 AND marks <= 100
marks = int(input("Enter your marks: "))

if marks >= 0:
    if marks <= 100:

        if marks >= 90:
            print("Excellent")
        elif marks >= 75:
            print("Very Good")
        elif marks >= 50:
            print("Good")
        else:
            print("Fail")

    else:
        print("Invalid Marks")
else:
    print("Invalid Marks")