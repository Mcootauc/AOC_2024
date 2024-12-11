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

# Initialize a similarity score and a hash map
similarity_score = 0
hash_map = {}

# Reads the content of the file Day1.txt
with open('Day1.txt', 'r') as file:
    for line in file:
        num1, num2 = map(int, line.split())
        # Add number to hash map if it doesn't exist and iterate the count if it does
        if (hash_map.get(num2) is None):
            hash_map[num2] = 1
        else:
            hash_map[num2] += 1

# Reads the content of the file Day1.txt
with open('Day1.txt', 'r') as file:
    for line in file:
        num1, num2 = map(int, line.split())
        # Checks if the number exists in the hash map, if it does, add the product of the number and the count to the similarity score
        if (hash_map.get(num1) is not None):
            similarity_score += hash_map[num1] * num1 
        else:
            continue

print(similarity_score) # Answer: 18934359