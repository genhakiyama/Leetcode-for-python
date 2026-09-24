class Solution:
    def climbStairs(self , n : int) -> int :
        dp = [int(0)] * (n + 1)

        dp[0] = 1
        for i in range(1 , n + 1) :
            if i >= 2 :
                dp[i] = dp[i] + dp[i - 2]
            if i >= 1 : 
                dp[i] = dp[i] + dp[i - 1]

        return dp[n]

n = int(input("n = "))
print(Solution().climbStairs(n))
