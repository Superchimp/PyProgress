grid = [[".", ".", ".", ".", ".", "."],
        [".", "O", "O", ".", ".", "."],
        ["O", "O", "O", "O", ".", "."],
        ["O", "O", "O", "O", "O", "."],
        [".", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "."],
        ["O", "O", "O", "O", ".", "."],
        [".", "O", "O", ".", ".", "."],
        [".", ".", ".", ".", ".", "."]]

def rotate_grid(image):
    image_line = ""
    x_length = len(image[0])
    y_length = len(image)
    for x in range(x_length):
        for y in range(y_length, 0, -1):
            image_line = image_line + image[y-1][x]
        
        print(image_line)
        image_line = ""
    
    
rotate_grid(grid)