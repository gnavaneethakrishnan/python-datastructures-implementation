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
    for i in range(len(nums) - 1):
        min_index: int = i
        for j in range(i + 1, len(nums)):
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


def merge(sorted_list1: List[int], sorted_list2: List[int]) -> List[int]:
    combined_list = []
    i = 0
    j = 0

    while i <= len(sorted_list1) - 1 and j <= len(sorted_list2) - 1:
        # print(sorted_list1[i])
        if sorted_list1[i] < sorted_list2[j]:
            combined_list.append(sorted_list1[i])
            i += 1
        else:
            combined_list.append(sorted_list2[j])
            j += 1

    while i < len(sorted_list1):
        combined_list.append(sorted_list1[i])
        i += 1

    while j < len(sorted_list2):
        combined_list.append(sorted_list2[j])
        j += 1
    return combined_list


def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) == 1:
        return nums
    mid_index = len(nums) // 2
    left = merge_sort(nums[:mid_index])
    right = merge_sort(nums[mid_index:])
    return merge(left, right)


# print(search_array([4, 5, 6, 77, 188, 200, 455], 200))
print(merge([5, 19, 20, 58, 88], [1, 5, 9, 39, 99, 100, 101]))
print(merge_sort([5, 88, 33, 54, 5, 1, 100, 76, 33]))


