# Part 1
total_safe_reports = 0

with open ('Day2.txt', 'r') as file:
    for line in file:
        report = [int(num) for num in line.split()]
        trend = None
        for i in range(len(report) - 1): # iterate through the report
            diff = report[i + 1] - report[i]
            if abs(diff) <= 3 and abs(diff) >= 1: # if difference is less than 3 or greater than 1 and not 0
                if trend is None: # sets the trend for the first time
                    trend = 'increasing' if diff > 0 else 'decreasing'
                elif (trend == 'increasing' and diff < 0) or \
                (trend == 'decreasing' and diff > 0): # if the trend changes, the report is not safe
                    break
            else: # if the difference is greater than 3 or 0, the report is not safe
                break
        else: # if the loop completes, the report is safe
            total_safe_reports += 1

print("P1 Total Safe Reports:", total_safe_reports) # With the puzzle input, the answer is 585

# # Part 2
total_safe_reports = 0

# checks if the report is safe with the removal of one level
def is_safe_with_removal(report): 
    if is_safe_report(report): 
        return True
    
    # iterates through removing one element at a time to check if the report is safe with that removal
    for i in range(len(report)): 
        if is_safe_report(report[:i] + report[i + 1:]):
            return True
        
    return False

def is_safe_report(report):
    trend = None
    for i in range(len(report) - 1): # iterate through the report
        diff = report[i + 1] - report[i]
        if 1 <= abs(diff) <= 3: # if difference is less than 3 or greater than 1 and not 0
            if trend is None: # sets the trend for the first time
                trend = 'increasing' if diff > 0 else 'decreasing'
            elif (trend == 'increasing' and diff < 0) or \
            (trend == 'decreasing' and diff > 0): # if the trend changes, the report is not safe
                return False
        else: # if the difference is greater than 3 or 0, the report is not safe
            return False
    return True

with open ('Day2.txt', 'r') as file:
    for line in file:
        report = [int(num) for num in line.split()]
        if is_safe_with_removal(report): 
            total_safe_reports += 1

print("P2 Total Safe Reports:", total_safe_reports) # With the puzzle input, the answer is 626