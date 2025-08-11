# Binary Search Approach

class Solution:
    def searchRange(self, nums, target):
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first_occurrence = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first_occurrence = mid
                    right = mid - 1  # look on the left side
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first_occurrence       
        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last_occurrence = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    last_occurrence = mid
                    left = mid + 1  # look on the right side
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last_occurrence       
        first = findFirst(nums, target)
        last = findLast(nums, target)       
        return [first, last] if first != -1 else [-1, -1]

# Linear Search
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

