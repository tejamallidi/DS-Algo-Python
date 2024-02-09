# class Solution:
#     def twoSum(self, nums, target):
#         # if input is empty list return empty list
#         if len(nums) <= 1:
#             return []
#         # In a dict store the
#         test_map = {}
#         for i in range(len(nums)):
#             print(test_map)
#             print('********')
#             req = target-nums[i]
#             if req in test_map:
#                 return [test_map[req], i]
#             test_map[nums[i]] = i


# print(Solution().twoSum([2, 7, 11, 15], 9))


# s = "W3ak"
# print(s.lower())


import re

input = " "

# \W is equivalent of [^a-zA-Z0-9], which excludes all numbers and letters. To remove '_' we have to add specifically.
s = re.sub(r'[\W_]', '', input.lower())
print(s)
