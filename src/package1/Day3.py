# Day 3 Part 1:
with open('Day3.txt', 'r') as file:
    total = 0
    for line in file:
        indices = []
        start = 0
        # Find all the indices of the string "mul(" within the line
        while start < len(line):
            index = line.find("mul(", start)
            if index == -1:
                break
            indices.append(index)
            start = index + 1
        
        # Iterate through the indices and calculate the product of the two numbers
        for i in indices:
            start = i + 4 # The index of the first number
            first_num = 0 
            for j in range(start, len(line)): # Find the index of the second number
                if line[j] == ')':
                    string = line[start:j] # Extract the two numbers Ex: mul(2,3) -> 2,3
                    break
            string = string.split(',') # Split the two numbers
            if string[0].isdigit() and string[1].isdigit():
                total += int(string[0]) * int(string[1])
    
    print("(Part 1) Total:", total) # The answer is: 170807108

# Day 3 Part 2:
with open('Day3.txt', 'r') as file:
    enable_mul = True 
    total = 0
    for line in file:
        start = 0
        # Finds the index of the string "don't()", "do()", and "mul("
        for i in range(len(line)):
            if line[i] == 'd' and line.find('don\'t()', i) == i: 
                enable_mul = False
            elif line[i] == 'd' and line.find('do()', i) == i:
                enable_mul = True
            elif line[i] == 'm' and enable_mul and line.find('mul(', i) == i:
                start = i + 4 # The index of the first number
                first_num = 0 
                for j in range(start, len(line)): # Find the index of the second number
                    if line[j] == ')':
                        string = line[start:j] # Extract the two numbers Ex: mul(2,3) -> 2,3
                        break
                string = string.split(',') # Split the two numbers
                if string[0].isdigit() and string[1].isdigit():
                    total += int(string[0]) * int(string[1])
    
    print("(Part 2) Total:", total) # The answer is: 74838033