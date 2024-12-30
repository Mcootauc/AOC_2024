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