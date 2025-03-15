class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def stealpossible(capability):
            count,i=0,0
            while i<len(nums):
                if nums[i]<=capability:
                    count+=1
                    i+=2
                else:
                    i+=1
            return count>=k
        l,r=min(nums),max(nums)
        while l<r:
            mid=l+(r-l)//2
            if stealpossible(mid):
                r=mid
            else:
                l=mid+1
        return l