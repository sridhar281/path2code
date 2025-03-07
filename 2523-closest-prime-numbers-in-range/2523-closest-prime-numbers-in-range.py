from typing import List

class Solution:
    def isprime(self, n: int) -> bool:
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6  
        return True

    def closestPrimes(self, left: int, right: int) -> List[int]:
        prev_prime = -1
        num1, num2 = -1, -1  
        min_diff = float('inf')

        for i in range(left, right + 1):
            if self.isprime(i):
                if prev_prime != -1 and (i - prev_prime) < min_diff:
                    num1, num2 = prev_prime, i
                    min_diff = i - prev_prime  
                prev_prime = i  

        return [num1, num2] if num1 != -1 else [-1, -1]

        


        