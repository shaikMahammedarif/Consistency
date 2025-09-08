from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def has_zero(x: int) -> bool:
            return '0' in str(x)

        for i in range(1, n):
            j = n - i
            if not has_zero(i) and not has_zero(j):
                return [i, j]
