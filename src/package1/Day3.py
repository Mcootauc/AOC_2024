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
with open('Day3.txt', 'r') as file:
    enable_mul = True
    total = 0
    for line in file:
        start = 0

        for i in range(len(line)):
            if line[i] == 'd' and line.find('don\'t()', i) == i:
                enable_mul = False
            elif line[i] == 'd' and line.find('do()', i) == i:
                enable_mul = True
            elif line[i] == 'm' and enable_mul and line.find('mul(', i) == i:
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
