# Part 1
total_safe_reports = 0
curr_list = []
total_list = []

with open ('Day2.txt', 'r') as file:
    for line in file:
        for num in line.split():
            curr_list.append(int(num))
        total_list.append(curr_list)
        curr_list = []

# Checks if the list is increasing safely
def check_increasing_safety(list):
    for i in range(len(list) - 1):
        if list[i + 1] - list[i] <= 0 or list[i + 1] - list[i] > 3:
            return False
    return True

# Checks if the report is decreasing safely
def check_decreasing_safety(list):
    for i in range(len(list) - 1):
        if list[i + 1] - list[i] >= 0 or list[i + 1] - list[i] < -3:
            return False
    return True

# Loops through the list of lists 
for i in range(len(total_list)):
    # Loops through the current list
    for j in range(len(total_list[i]) - 1):
        # if difference between two numbers is greater than 3 or less than 1 then report is not safe
        if (abs(total_list[i][j + 1] - total_list[i][j]) > 3 or abs(total_list[i][j + 1] - total_list[i][j]) < 1):
            break
        elif (total_list[i][j + 1] - total_list[i][j] > 0): # if difference is positive then check if increasing safely
            if check_increasing_safety(total_list[i]) == True:
                total_safe_reports += 1
            break
        elif (total_list[i][j + 1] - total_list[i][j] < 0): # if difference is negative then check if decreasing safely
            if check_decreasing_safety(total_list[i]) == True:
                total_safe_reports += 1
            break

print("Total Safe Reports:", total_safe_reports) # With the puzzle input, the answer is 585