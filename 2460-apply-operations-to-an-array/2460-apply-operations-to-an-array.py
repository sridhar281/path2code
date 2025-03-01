class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=2*nums[i]
                nums[i+1]=0
            else:
                continue 
        a=[]
        c=0
        for i in range(len(nums)):
            if nums[i]>0:
                a.append(nums[i])
            else:
                c+=1
        b=[0]*c
        return a+b