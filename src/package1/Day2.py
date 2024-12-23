# Part 1
total_safe_reports = 0

with open ('Day2.txt', 'r') as file:
    for line in file:
        curr_list = [int(num) for num in line.split()]
        trend = None
        for i in range(len(curr_list) - 1): # iterate through the report
            diff_between_nums = curr_list[i + 1] - curr_list[i]
            if abs(diff_between_nums) <= 3 and abs(diff_between_nums) >= 1: # if difference is less than 3 or greater than 1 and not 0
                if trend is None: # sets the trend for the first time
                    trend = 'increasing' if diff_between_nums > 0 else 'decreasing'
                elif (trend == 'increasing' and diff_between_nums < 0) or \
                (trend == 'decreasing' and diff_between_nums > 0): # if the trend changes, the report is not safe
                    break
            else: # if the difference is greater than 3 or 0, the report is not safe
                break
        else: # if the loop completes, the report is safe
            total_safe_reports += 1

print("Total Safe Reports:", total_safe_reports) # With the puzzle input, the answer is 585

# # Part 2
# total_safe_reports = 0

# with open ('Day2.txt', 'r') as file:
#     for line in file:
#         curr_list = [int(num) for num in line.split()]
#         trend = None
#         removal = 0
#         for i in range(len(curr_list) - 1): # iterate through the report
#             diff_between_nums = curr_list[i + 1] - curr_list[i]
#             if abs(diff_between_nums) <= 3 and abs(diff_between_nums) >= 1: # if difference is less than 3 or greater than 1 and not 0
#                 if trend is None: # sets the trend for the first time
#                     trend = 'increasing' if diff_between_nums > 0 else 'decreasing'
#                 elif (trend == 'increasing' and diff_between_nums < 0 and removal == 0) or \
#                 (trend == 'decreasing' and diff_between_nums > 0 and removal == 0): # if the trend changes, the report is not safe
#                     removal += 1
#                     print("removal", removal)
#                 elif (trend == 'increasing' and diff_between_nums < 0 and removal == 1) or \
#                 (trend == 'decreasing' and diff_between_nums > 0 and removal == 1): # if the trend changes, the report is not safe
#                     break
#             elif removal == 0:
#                 removal += 1
#                 print("removal", removal)
#             else: # if the difference is greater than 3 or 0, the report is not safe
#                 break
#         else: # if the loop completes, the report is safe
#             total_safe_reports += 1
            
# print("Total Safe Reports:", total_safe_reports)