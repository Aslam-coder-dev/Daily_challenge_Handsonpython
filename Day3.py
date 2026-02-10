n = int(input("Enter number of students: "))
marks = []
for i in range(n):
    m = int(input(f"Enter mark {i+1}: "))
    marks.append(m)
valid_students = 0
failed = 0
for mark in marks:
    if mark < 0 or mark > 100:
        print(mark, "→ Invalid")
    else:
        valid_students = valid_students + 1
        if mark>=90 and mark<=100:
            print(mark, "→ Excellent (Lucky bonus will be given to you around 5k)")
        elif mark>=75 and mark<=89:
            print(mark, "→ Very Good")
        elif mark>=60 and mark<=74:
            print(mark, "→ Good")
        elif mark>=40 and mark<=59:
            print(mark, "→ Average")
        else:
            print(mark, "-> Fail")
            failed = failed + 1
print("Final summary:")
print("Total Valid Students:", valid_students)
print("Total Failed Students:", failed)
