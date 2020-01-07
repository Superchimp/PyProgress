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
    for i in table:      # looping through inner tables
        for j in i:      # looping through string in the inner list
            for c in j:  # looping through each character in the string
                counter = counter + 1
        print ("list:", i, "contains", counter, "characters")
        if counter >= maximum_length:  # check total number of characters counted in the inner list is a new record
           maximum_length = counter
        counter = 0
            
    print ("Maximum character spaces needed: " + str(maximum_length))
    
    # Printing the table correctly (Right Justified)
    
    for l in table:
        text = " ".join(l)  # put the list strings together ready to print
        print(text.rjust(maximum_length + 3))   # add 3 for the 3 spaces just added when joining the list strings
        


def print_Table_v2(table):
    
    new_table = []              # hold our reordered table for later printing plus length storage
    
    for i in range(len(table[0])):     # makes the same amount of nested lists as source table
        new_table.append([])
        
    for y in range(len(table)):
        for x in range(3):
            current = table[x][y]
            new_table[y].append(current)
            print (x,y)
        
    print(new_table)    
    
    printTable(new_table)
    
    
    
            
if __name__ == "__main__":
    printTable(tableData)
    print_Table_v2(tableData)