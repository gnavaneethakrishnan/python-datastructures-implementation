from typing import List


def insertion_sort(nums: List[int]) -> List[int]:
    for index in range(1, len(nums)):
        j = index - 1
        while j >= 0 and nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            j -= 1
    return nums


print(insertion_sort([3, 54, 48, 1, 9]))


def bubble_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
    return nums


print(bubble_sort([3, 5, 10, 98, 45, 1, 100]))


def selection_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums)-1):
        min_index: int = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


print(selection_sort([100, 6, 90, 1, 88]))


def search_array(nums: List[int], target: int) -> int:
    left = nums[0]
    right = len(nums) - 1
    mid = (left + right) // 2
    while left <= right:
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1


print(search_array([4, 5, 6, 77, 188, 200, 455], 200))
