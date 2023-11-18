total_number_of_tasks = 10

correctly_completed_tasks = 4

grade = correctly_completed_tasks/total_number_of_tasks

if grade >= 0.5:
    print(f"Test passed!")
else:
    print(f"Test failed!")