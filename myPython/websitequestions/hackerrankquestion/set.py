nums = [1, 2, 3, 1, 5, 6, 6, 7, 8]
set_list = []
repeated_element = []
for i in nums:
    if i in repeated_element:
        continue
    counter = 0
    for j in nums[nums.index(i) + 1 : ]:
        if i == j:
            repeated_element.append(i)
            counter += 1

    if counter == 0:
        set_list.append(i)

print(set_list)

