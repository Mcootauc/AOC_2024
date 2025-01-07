# Day 5 Part 1
dict_of_rules = {}
total = 0

with open("Day5.txt", 'r') as file:
    rules, updates = file.read().strip().split("\n\n") # Split the file into rules and queries based on the new line in between
    for rule in rules.split("\n"):
        num1, num2 = rule.split('|') # Split the rule into two numbers
        num1, num2 = int(num1), int(num2)
        dict_of_rules.setdefault(num1,[]).append(num2)
    
    for update in updates.split("\n"):
        ordered = True 
        list_of_page_nums = [int(num) for num in update.split(",")] # Split the update into a list of numbers based on the comma
        for i in range(len(list_of_page_nums)): 
            for j in range(i + 1, len(list_of_page_nums)):
                if list_of_page_nums[j] not in dict_of_rules.get(list_of_page_nums[i], []): # Confirms that the numbers in front of the number at index i are in the list of numbers that can come after it
                    ordered = False
                    break
        if ordered:
            total += list_of_page_nums[len(list_of_page_nums) // 2] # Add the middle number to the total
    
    print("(Part 1) Sum total of all correctly-ordered updates:", total)  # The answer is 4774

# Day 5 Part 2
dict_of_rules = {}
total = 0

def correct_updates(start, list_of_page_nums):
    if start == len(list_of_page_nums): # If the start is equal to the length of the list of page numbers, return the middle number
        return list_of_page_nums[len(list_of_page_nums) // 2]
    for i in range(start, len(list_of_page_nums)): # 
        for j in range(i + 1, len(list_of_page_nums)):
            if list_of_page_nums[j] not in dict_of_rules.get(list_of_page_nums[i], []): # Confirms that the numbers in front of the number at index i are in the list of numbers that can come after it
                if (list_of_page_nums[i] in dict_of_rules.get(list_of_page_nums[j], [])): # If the number at index i can come after the number at index j, swap the numbers
    
                    list_of_page_nums[i], list_of_page_nums[j] = list_of_page_nums[j], list_of_page_nums[i] # Swap the numbers
                    return correct_updates(start, list_of_page_nums) # Recursively call the function to sort again
    return list_of_page_nums[len(list_of_page_nums) // 2] # Recursively call the function

with open("Day5.txt", 'r') as file:
    rules, updates = file.read().strip().split("\n\n") # Split the file into rules and queries based on the new line in between
    for rule in rules.split("\n"):
        num1, num2 = rule.split('|') # Split the rule into two numbers
        num1, num2 = int(num1), int(num2)
        dict_of_rules.setdefault(num1,[]).append(num2)
        
    for update in updates.split("\n"):
        ordered = True 
        start = 0
        list_of_page_nums = [int(num) for num in update.split(",")] # Split the update into a list of numbers based on the comma
        for i in range(len(list_of_page_nums)): 
            for j in range(i + 1, len(list_of_page_nums)):
                if list_of_page_nums[j] not in dict_of_rules.get(list_of_page_nums[i], []): # Confirms that the numbers in front of the number at index i are in the list of numbers that can come after it
                    start = i
                    ordered = False
                    break
            if not ordered: # If the list is not ordered, break out of the loop
                break
    
        if not ordered:
            total += correct_updates(start, list_of_page_nums) # Add the middle number to the total
    
    print("(Part 2) Sum total of all post-corrected updates:", total)  # The answer is 6004