spam = ["apples", "bananas", "tofu", "cats"]
eggs =[16, "Oranges", 35, "Kiwi", 100.99]

def comma_and(ham):
    length = len(ham)
    output = ""
    for i in range(length):
        if i == 0:
            print(str(ham[0]), end="")
        elif i == length -1:
            print(" and " + str(ham[-1]))
        else:
            print (", " + str(ham[i]), end="")
        
comma_and(spam)
comma_and(eggs)
    