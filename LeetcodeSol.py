class Solution:
    def __init__(self) -> None:
        pass

    # problem1 two sum
    @staticmethod
    def twosum(nums,target): 
        for i in range(len(nums)-1):
            if nums[i]+nums[i+1]==target:
                return [i,i+1]



