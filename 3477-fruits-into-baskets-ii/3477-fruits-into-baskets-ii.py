class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n=len(fruits)
        m=len(baskets)
        unplaced = 0
        for i in range(n):
            placed=False
            for j in range(m):
                if baskets[j]>=fruits[i]:
                    baskets[j]=-1
                    placed=True
                    break
            if not placed:
                unplaced+=1
        return unplaced