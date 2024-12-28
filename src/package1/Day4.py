def check_horizontal(start, line):
    # Grabs the 4 letter string from left to right
    string = ''.join(line[start:start + 4])
    if (line[start] == 'X' and string == 'XMAS') or (line[start] == 'S' and string == 'SAMX'):
        return True
    return False

def check_vertical(line_start, char_start,  whole_list):
    string = ''
    # Grabs the 4 letter string from top to bottom
    for i in range(4):
        string += whole_list[line_start + i][char_start]
    
    if (whole_list[line_start][char_start] == 'X' and string == 'XMAS') or (whole_list[line_start][char_start] == 'S' and string == 'SAMX'):
        return True
    return False

def check_diagonal_top_right_to_bot_left(line_start, char_start, whole_list):
    string = ''
    # Grabs the 4 letter string from top right to bottom left
    for i in range(4):
        string += whole_list[line_start + i][char_start - i]
    
    if (whole_list[line_start][char_start] == 'X' and string == 'XMAS') or \
        (whole_list[line_start][char_start] == 'S' and string == 'SAMX'):
        return True

    return False

def check_diagonal_top_left_to_bot_right(line_start, char_start, whole_list):
    string = ''
    # Grabs the 4 letter string from top left to bottom right
    for i in range(4):
        string += whole_list[line_start + i][char_start + i]

    if (whole_list[line_start][char_start] == 'X' and string == 'XMAS') or \
        (whole_list[line_start][char_start] == 'S' and string == 'SAMX'):
        return True
    
    
    return False
    

with open('Day4.txt', 'r') as file:
    word_count = 0

    # Reads the file and creates a 2D list
    whole_list = [[char for char in line if char != '\n'] for line in file]
    for i in range(len(whole_list)):
        for j in range(len(whole_list[i])):
            if j < len(whole_list[i]) - 3 and (whole_list[i][j] == 'X' or whole_list[i][j] == 'S') and check_horizontal(j, whole_list[i]):
                word_count += 1
            if i < len(whole_list) - 3 and (whole_list[i][j] == 'X' or whole_list[i][j] == 'S') and check_vertical(i, j, whole_list):
                word_count += 1
            if i < len(whole_list) - 3 and 3 <= j and (whole_list[i][j] == 'X' or whole_list[i][j] == 'S') and check_diagonal_top_right_to_bot_left(i, j, whole_list):
                word_count += 1
            if i < len(whole_list) - 3 and j < len(whole_list[i]) - 3 and (whole_list[i][j] == 'X' or whole_list[i][j] == 'S') and check_diagonal_top_left_to_bot_right(i, j, whole_list):
                word_count += 1

    print("(Part 1) XMAS is found the following number of times:", word_count) # The answer is 2547