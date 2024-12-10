# Reads the content of the file Day1.txt
with open('Day1.txt', 'r') as file:
    lines = file.readlines()

# Initializes the variables
total_distance = 0
list_1 = []
list_2 = []

# Removes the whitespace and adds the first number to list_1 and the second number to list_2
for line in lines:
    numbers = [int(num) for num in line.split()]
    list_1.append(numbers[0])
    list_2.append(numbers[1])

# Sorts the lists
list_1.sort()
list_2.sort()

# Calculates the total distance
for i in range(len(list_1)):
    total_distance += abs(list_1[i] - list_2[i])

print(total_distance)