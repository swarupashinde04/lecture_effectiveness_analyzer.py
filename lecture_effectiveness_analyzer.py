# lecture effectiveness analyzer 
# Author : Swarupa

# building a function :

def lecture_effectiveness(duration, interaction, sleepiness):

    # Duration score
    if 45 <= duration <= 60:
        duration_score = 10
    else:
        duration_score = max(0, 10 - abs(duration - 52) / 5)

    effectiveness = (
        interaction * 0.5 +
        duration_score * 0.3 +
        (10 - sleepiness) * 0.2
    )

    percentage = (effectiveness / 10) * 100

    if percentage >= 75:
        feedback = "Highly effective lecture."
    elif percentage >= 50:
        feedback = "Moderately effective. Increase interaction."
    else:
        feedback = "Low effectiveness. Lecture redesign suggested."

    return round(percentage, 2), feedback


# USER INPUT
duration = int(input("Lecture duration (minutes): "))
if duration <=0 :
    print("Invalid input.")
    exit()
interaction = int(input("Interaction level (1-10): "))
if interaction <1 or interaction >10 :
    print("Invalid input.")
    exit()
sleepiness = int(input("Sleepiness level (1-10): "))
if sleepiness <1 or sleepiness >10 :
    print("Invalid input.")
    exit()

score, feedback = lecture_effectiveness(duration, interaction, sleepiness)

print(f"Lecture Effectiveness: {score}%")
print(f"Feedback: {feedback}")
