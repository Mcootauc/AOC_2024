# Day 3 Part 1:

with open('Day3.txt', 'r') as file:
    total = 0
    for line in file:
        indices = []
        start = 0
        while start < len(line):
            index = line.find("mul(", start)
            if index == -1:
                break
            indices.append(index)
            start = index + 1
        
        for i in indices:
            start = i + 4
            first_num = 0
            for j in range(start, len(line)):
                if line[j] == ')':
                    string = line[start:j]
                    break
            string = string.split(',')
            if string[0].isdigit() and string[1].isdigit():
                total += int(string[0]) * int(string[1])
    
    print("The total is: ", total) # The answer is: 170807108

# Day 3 Part 2: