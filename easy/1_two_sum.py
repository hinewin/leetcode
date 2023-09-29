from typing import List
nums = [3,3,4]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in range(len(nums) - 1):
            for b in range(a+1, len(nums)):
                if nums[a] + nums[b] == target:
                    pass



solution = Solution()

#print (solution.twoSum(nums, 6))

#Brute Force/ O(n^2) trying every element in a For loop twice

for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        print (j)
        