grade = int(input("What is your score? "))

if grade > 100 or grade < 0:
    letter = "an invalid score."
elif grade >= 90:
    letter = "A"
elif grade >= 80 and grade < 90:
    letter = "B"
elif grade >= 70 and grade < 80:
    letter = "C"
elif grade >= 60 and grade < 70:
    letter = "D"
elif grade < 60 and grade >= 0:
    letter = "F"

    
print("Your grade is", letter)