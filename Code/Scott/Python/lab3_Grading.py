#Lab3_Grading.py
#Grades.py
numeric_score = input("What is your numeric score?")
numeric_score = int(numeric_score)
suffix = ''
suffix_plus = '+'
suffix_minus = '-'
if numeric_score % 10 > 7:
    suffix = suffix_plus
if numeric_score % 10 < 3:
    suffix = suffix_minus
if numeric_score > 89:
    print("Your grade is an A" + suffix)
elif numeric_score > 79:
    print("Your grade is a B" + suffix)
elif numeric_score > 69:
    print("Your grade is a C" + suffix)
elif numeric_score > 59:
    print("Your grade is a D" + suffix + "You still pass!")
elif numeric_score < 60:
    print("See you next year!")

