# returns k largest integers present in nums
def printKLargest(nums, k):
    result = []
    for i in range(0, k):
        result.append(max(nums))
        nums.remove(max(nums))

    return result


print(printKLargest([1, 23, 12, 9, 2, 50], 3))
