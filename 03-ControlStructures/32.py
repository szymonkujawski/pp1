first_question = (input("Are you interested in computer science? (Y/N): "))
second_question = (input("Do you like playing computer games? (Y/N): "))
third_question = (input("Do you have an Instagram account? (Y/N): "))

if first_question.upper()=="Y":
    print("Interested in computer science: Yes")
elif first_question.upper()=="N":
    print("Interested in computer science: No")
else:
    print("Wrong answer! Use Y or N")

if second_question.upper()=="Y":
    print("Playing computer games: Yes")
elif second_question.upper()=="N":
    print("Playing computer games: No")
else:
    print("Wrong answer! Use Y or N")

if third_question.upper()=="Y":
    print("Has an Instagram account: Yes")
elif third_question.upper()=="N":
    print("Has an Instagram account: No")
else:
    print("Wrong answer! Use Y or N")

