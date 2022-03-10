def twoSum(nums:list, target: int) -> list:
    nums_dict = {}
    for i, num in enumerate(nums):
        nums_dict[num] = i
        if target - num in nums_dict and nums_dict[target - num] != i:
            return [i, nums_dict[target-num]]

print(twoSum(nums=[2,7,11,15], target=9))