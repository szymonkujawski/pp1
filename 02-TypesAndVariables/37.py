personal_data = "Mr. John May, born on 1998-02-16"

personal_data_without_mr = (personal_data.split("."))[1]
personal_data_without_mr = personal_data_without_mr.strip()

name = (personal_data_without_mr.split(" "))[0]
surname = (personal_data_without_mr.split(" "))[1]
surname = surname[:-1]

born = personal_data_without_mr[-10:]

print(f"Description: {personal_data}")
print(f"Name: {name}")
print(f"Surname: {surname}")
print(f"Born: {born}")