# declare initial variable value
total = 0
# create a For Loop to iterate through each of the values in a defined Range
for num in range(101):
    # for each value in the range, add it to the combined values
    total = total + num
    # print to screen the present number and the present sub-total
    print(f'Current number: {num} & current sub-total = {total}')
# print the collective total after iterating through the entire Range
print(f'The complete total is: {total}')
