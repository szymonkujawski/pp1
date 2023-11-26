def count(file):
    file = open(file, "r")
    count_lines = 0
    for line in file:
        count_lines += 1
    return f"Number of lines: {count_lines}"

nazwa = input(str("Wprowadź nazwę pliku: "))
print(count(nazwa))