def check_if_binary(binary_number):
    for number in binary_number:
        if number not in ['0', '1']:
            return False
    return True

binary_number = "101010111100101"

print(check_if_binary(binary_number))