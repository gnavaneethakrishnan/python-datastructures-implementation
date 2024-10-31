from typing import List


def insertion_sort(nums: List[int]) -> List[int]:
    for index in range(1, len(nums)):
        j = index - 1
        while j >= 0 and nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            j -= 1
    return nums



print(insertion_sort([3, 54, 48, 1, 9]))
