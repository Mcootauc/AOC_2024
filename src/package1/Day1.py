# Day 1 Part 1:
# Initialize two lists
list_1 = []
list_2 = []

# Reads the content of the file Day1.txt
with open('Day1.txt', 'r') as file:
    for line in file:
        num1, num2 = map(int, line.split())
        list_1.append(num1)
        list_2.append(num2)

# Sorts the lists
list_1.sort()
list_2.sort()

# Calculates the total distance
total_distance = sum(abs(a - b) for a, b in zip(list_1, list_2))

print(total_distance) # Answer: 2378066

# Day 1 Part 2:
from collections import defaultdict

# Initialize a hash map with default value of 0 and a similarity score
hash_map = defaultdict(int)
similarity_score = 0

# Reads the content of the file Day1.txt
with open('Day1.txt', 'r') as file:
    for line in file:
        _, num2 = map(int, line.split())
        # Count how often each number appears in the right list
        hash_map[num2] += 1

# Reads the content of the file Day1.txt
with open('Day1.txt', 'r') as file:
    for line in file:
        num1, _ = map(int, line.split())
        # Checks if the number exists in the hash map, if it does, add the product of the number and the count to the similarity score
        if hash_map[num1] is not None:
            similarity_score += num1 * hash_map[num1]
        else:
            continue

print(similarity_score) # Answer: 18934359