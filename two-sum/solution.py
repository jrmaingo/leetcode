class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        sorted_nums = mergesort(nums)
        for index_a in range(len(sorted_nums)):
            target_b = target - sorted_nums[index_a]
            index_b = binsearch(sorted_nums, target_b)
            if index_b != -1:
                return linsearch(nums, sorted_nums[index_a], sorted_nums[index_b])
        return [-1, -1]

def linsearch(nums, target_a, target_b):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    result = []
    for index in range(len(nums)):
        if len(result) == 2:
            break;
        if nums[index] == target_a:
            result.append(index)
        if nums[index] == target_b and (target_a != target_b or result[0] != index):
            result.append(index)
    return result

def binsearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    index = len(nums) // 2
    index_min = -1
    index_max = len(nums)
    while index > index_min and index < index_max:
        if nums[index] == target:
            return index
        elif nums[index] > target:
            index_max = index
            index //= 2
        else:
            index_min = index
            index = (index + len(nums)) // 2
    return -1

def mergesort(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    def merge(list_a, list_b):
        """
        :type list_a: List[int]
        :type list_b: List[int]
        :rtype: List[int]
        """

        index_a = index_b = 0
        list_result = []
        while index_a < len(list_a) or index_b < len(list_b):
            if index_a == len(list_a):
                list_result += list_b[index_b:]
                break
            elif index_b == len(list_b):
                list_result += list_a[index_a:]
                break
            elif list_a[index_a] > list_b[index_b]:
                list_result.append(list_b[index_b])
                index_b += 1
            else:
                list_result.append(list_a[index_a])
                index_a += 1
        return list_result

    if len(nums) == 1:
        return nums
    else:
        midpoint = len(nums) // 2
        list_left = nums[:midpoint]
        list_right = nums[midpoint:]
        slist_left = mergesort(list_left)
        slist_right = mergesort(list_right)
        merged =  merge(slist_left, slist_right)
        return merged
