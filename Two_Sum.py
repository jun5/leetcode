
'''
Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a
specific target.
You may assume that each input would have exactly one solution.
Example: ```Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,```
return [0, 1]. UPDATE (2016/2/13): The return format had been changed to zero-based
indices. Please read the above updated description carefully.
'''
def two_sum():
	array_input = input("the list you want to input:")

	dict1 = {}

	for i in range(len(array_input)):
		item = array_input[i]
		dict1[item] = i

	target = input("the target number u input: ")

	for j in range(len(array_input)):
		item2 = array_input[j]
		if target - item2 in dict1:
			z = dict1[target - item2]
			if j != z:
				return [j,z]
