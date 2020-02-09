result = ""

for i in range(1, 50):
    if i % 3 == 0:
        result = result + "Fizz "
    if i % 5 == 0:
        result = result + "Buzz "
    if result == "":
        result = str(i)
    print(result)
    result = ""