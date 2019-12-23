

def binary2decimal (binary_num):
    counter = 0
    result = 0
    for i in reversed(binary_num):
        result = result + int(i) * 2 ** counter
        counter = counter + 1
    return result


if __name__ == "__main__":
    user_input = input("Please Enter Binary Number: ")
    print("Decimal: \t \t", binary2decimal(user_input))
    print("Octal (0o): \t \t", oct(binary2decimal(user_input)).lstrip("0o"))
    print ("Hexidecimal (0x): \t", hex(binary2decimal(user_input)).lstrip("0x"))