"""Objective:
Make a function that takes a list of strings and displays it in a well-organised
table with each column right-justified. Assume that all inner lusts will contain
the same number of strings."""

# Example list
tableData = [["apples", "oranges", "cherries", "banana"],
             ["Alice", "Bob", "Carol", "David"],
             ["dogs", "cats", "moose", "goose"]]

def printTable(table):
    maximum_length = 0
    counter = 0
    # First find the max character length of the longest 4 item inner list to know how much space we need
    for i in table:
        for j in i:
            for c in j:
                counter = counter + 1
        print ("list:", i, "contains", counter, "characters")
        if counter >= maximum_length:
           maximum_length = counter
        counter = 0
            
    print ("Maximum character spaces needed: " + str(maximum_length))    
            
            
if __name__ == "__main__":
    printTable(tableData)