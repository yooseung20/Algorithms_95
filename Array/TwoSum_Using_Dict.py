def twoSum(nums:list, target:int) -> list:
    nums_map ={} # key = num, value = index
    for i, num in enumerate(nums):
        nums_map[num] = i
    
    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i,nums_map[target-num]]

print(twoSum(nums=[2,7,11,15], target=9))            
