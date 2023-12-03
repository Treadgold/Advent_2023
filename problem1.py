import os

data = {}
with open('input.txt', 'r') as f:
    count = 0
    for line in f:
        count += 1
        data[count] = line
    
    
answer = 0
for item in data.items():
    nums = []
    i = item[1]
    for char in i:
        # check if char is a digit
        if char.isdigit():
            if nums == []:
                nums.append(char)
            elif len(nums) == 1:
                nums.append(char)
            elif len(nums) == 2:
                nums[1] = char
    if len(nums) == 1:
        nums.append(nums[0])
    #print(nums)
    answer += (int(nums[0])*10) + int(nums[1])

print(f"{answer=}")       
