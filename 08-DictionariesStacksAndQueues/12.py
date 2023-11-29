import json
student = {
    "Age":20,
    "Good_student":False,
    "Name":"Szymon",
    "Grades":[3,3,3,3],
    "Appear":{
                "Hair":"Blonde",
                "Height":175
            }
}

file = open("student.json", "w")

json.dump(student, file, indent=6)

file.close()