class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {}

        for i, elem in enumerate(nums):
            compliment = target - elem
            if compliment in hashmap:
                return [hashmap[compliment], i]
            hashmap[elem] = i
