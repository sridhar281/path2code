class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        a=[]
        tc=0
        if len(nums)==1 and nums[0]==0:
            return 1
        for i in range(len(nums)):
            if nums[i]==0 and (i == 0 or nums[i-1] != 0):
                cnt=0
                for j in range(i,len(nums)):
                    if nums[j]==0:
                        cnt+=1
                    else:
                        break
                a.append([0]*cnt)
        for i in a:
            n=len(i)
            tc+=(n*(n+1))//2
        return tc



                


           