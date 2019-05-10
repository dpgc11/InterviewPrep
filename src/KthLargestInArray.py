# returns kth largest integer present in nums
def printKthLargest(nums, k):
    result = nums[0]
    for i in range(0, k):
        result = max(nums)
        nums.remove(max(nums))

    return result


print(printKthLargest([1, 23, 12, 9, 2, 50], 4))
