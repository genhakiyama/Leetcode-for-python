import math
import ast
import json 

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices) 
        max_value = [float(-1e9)] * (n + 1)

        for i in range(n - 1 , 0 , -1) : 
            max_value[i] = max(max_value[i + 1] , prices[i])

        min_value = float(1e9)
        ans = 0

        for i in range(0 , n , 1) :
            min_value = min(min_value , prices[i]) 
            ans = max(ans , max_value[i + 1] - min_value)

        return ans 

user_input = input()
# arr = [int(x) for x in user_input.strip("[]").split(",") if x.strip()]
# arr = ast.literal_eval(user_input)
# arr = json.loads(user_input)

# print(arr)
# print(Solution().maxProfit(arr))