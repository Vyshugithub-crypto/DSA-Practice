"""
=========================================
DAY 02 - TWO POINTER PATTERN
=========================================

Problems Solved:
1. Move Zeroes
2. Remove Duplicates from Sorted Array
3. Merge Two Sorted Arrays
"""

# =========================================
# 1. Move Zeroes
# =========================================

def move_zeroes(arr):
    left = 0

    for right in range(len(arr)):
        if arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1

    return arr


# Example
arr = [0, 1, 0, 3, 12]
print("Move Zeroes:", move_zeroes(arr))


# =========================================
# 2. Remove Duplicates from Sorted Array
# =========================================

def remove_duplicates(arr):
    if len(arr) == 0:
        return 0

    left = 0

    for right in range(1, len(arr)):
        if arr[left] != arr[right]:
            left += 1
            arr[left] = arr[right]

    return left + 1


# Example
arr = [1, 1, 2, 2, 3, 4, 4]
k = remove_duplicates(arr)
print("Unique Elements:", arr[:k])


# =========================================
# 3. Merge Two Sorted Arrays
# =========================================

def merge_sorted_arrays(arr1, arr2):
    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


# Example
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

print("Merged Array:", merge_sorted_arrays(arr1, arr2))
