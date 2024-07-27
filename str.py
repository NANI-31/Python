# def solution(str1,str2):
#     if len(str1) != len(str2):
#         return False
#     for i in range(len(str1)):
#         if str1[i] == str2[i]:
#             continue
#         j = j+1
# nums = [1,2,3,3]
# class Solution:
#     def hasDup(self, nums):
#         index = 0
#         def dfs(nums,i, index):
#             l = index
#             c = 0
#             for j in nums:
#                 if i == j:
#                     c = c + 1
#             if c > 1:
#                 return True
#             else:
#                 l = l+1
#                 if l < len(nums):
#                     return dfs(nums, nums[l], l)
#                 return False
#         if dfs(nums, nums[0], index):
#             return True
#         else:
#             return False
# s = Solution()
# print(s.hasDup(nums))

n = 1000033
for i in range(2, n):
    if n%i == 0:
        print("not a prime")
else:
    print