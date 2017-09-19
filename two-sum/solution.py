class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        sortedList = mergesort(nums)

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
                break;
            elif index_b == len(list_b):
                list_result += list_a[index_a:]
                break;
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

mysoln = Solution()
ulist = [1, 3, 2, 9, 5, 11, 8]
sorted = mergesort(ulist)
print(ulist)
print(sorted)
