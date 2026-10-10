
score = int(input("What is your score? "))

def get_letter_grade(score):

    if score > 100 or score < 0:
        letter = "an invalid score."
    elif score >= 90:
        letter = "A"
    elif score >= 80 and score < 90:
        letter = "B"
    elif score >= 70 and score < 80:
        letter = "C"
    elif score >= 60 and score < 70:
        letter = "D"
    elif score < 60 and score >= 0:
        letter = "F"

    return letter


letter = get_letter_grade(score)

print("Your grade is", letter)