class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
      def findfir(nums,target):
         l,r=0,len(nums)-1
         fir=-1 
         while l<=r:
                mid=l+(r-l)//2 
                if nums[mid]==target:
                    fir=mid 
                    r=mid-1 
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1 
         return fir 
      def findlas(nums,target):
            l,r=0,len(nums)-1
            las=-1
            while l<=r:
                mid=l+(r-l)//2
                if nums[mid]==target:
                    las=mid 
                    l=mid+1
                elif nums[mid]<target:
                    l=mid+1 
                else:
                    r=mid-1 
            return las 
      fir=findfir(nums,target)
      las=findlas(nums,target)
      return [fir,las]
