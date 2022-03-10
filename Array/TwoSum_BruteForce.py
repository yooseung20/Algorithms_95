def twoSum(nums:list, target:int) -> list : # 두수의 index 리턴 
    for i in range(0, len(nums) -1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    
    return False

print(twoSum(nums=[2,7,11,15], target=9))

