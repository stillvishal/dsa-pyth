class Solution():
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.

        :param nums: List of integers
        :param target: Integer target
        :return: List of indices of the two numbers that add up to target
        """
        num_to_index = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index
        
        return []  # In case there is no solution, though the problem guarantees one solution.