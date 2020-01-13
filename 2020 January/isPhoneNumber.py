import re


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[0].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range (8,12):
        if not text[i].isdecimal():
            return False
    return True

print("415-555-4242 is a phone number:")
print(isPhoneNumber("415-555-4242"))
print("Moshi Moshi is a Phone Number:")
print(isPhoneNumber("Moshi Moshi"))
print("o----------------------------o")


message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone number found: " + chunk)
        
print("Done")
print("o----------------------------o")
#                                                                               3      3       4
phoneNumRegex = re.compile(r"\d{3}-\d{3}-\d{4}")            # alternative to \d\d\d-\d\d\d-\d\d\d\d
mo = phoneNumRegex.search("My number is 415-555-4242 or 415-555-2424")
print("Phone number found:", mo.group())

print("o----------------------------o")

phoneNumRegex = re.compile(r"(\d{3})-(\d{3}-\d{4})")         # alternative to (\d\d\d)-(\d\d\d-\d\d\d\d)
mo = phoneNumRegex.search("My number is 415-555-4242.")
print("print all match objects:", mo.group(0))
print("print match object 1:", mo.group(1))
print("print match object 2:", mo.group(2))
print("print match object groups:", mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

print("o----------------------------o")

phoneNumRegex = re.compile(r"(\(\d{3}\)) (\d{3}-\d{4})")
mo = phoneNumRegex.search("My phone number is (415) 555-4242.")
print("print group 1:", mo.group(1))
print("print group 2:", mo.group(2))
print("print all groups:", mo.group(0))