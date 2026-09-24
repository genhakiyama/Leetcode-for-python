import math

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        cnt = 0 
        ans = 0

        for i in nums :
            if (i == 0) :
                cnt = 0
            else :
                cnt = cnt + 1
            ans = max(ans , cnt)

        return ans

n = list(map(int , input().split()))
sol = Solution()
print(sol.findMaxConsecutiveOnes(n))