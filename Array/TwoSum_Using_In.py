def twoSum(nums = list, target=int) -> list :
    for i, n in enumerate(nums):
        temp = target - n # 필요한 값을 저장한다.

        if temp in nums[i+1:]:  
            return [i, nums.index(temp)]

print(twoSum(nums=[2,7,11,15], target=13))