class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n>1 and n%4==1:
            return False
        while(n>1):
            n=n//4
        if n==1:
            return True
        else:
            return False