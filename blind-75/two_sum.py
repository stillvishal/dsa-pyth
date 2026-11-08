
#BRUTE FORCE

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

#OPTIMIZED
class Solution(object):
    def twoSum(self, nums, target):
        dict_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in dict_map:
                return [i, dict_map[complement]]
            dict_map[num] = i


solution = Solution()
answer = solution.twoSum([2, 7, 11, 15], 9)
print(answer)  