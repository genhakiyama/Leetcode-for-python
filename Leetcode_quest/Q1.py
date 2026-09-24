class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        nums.extend(nums)
        return nums

sol = Solution()
n = list(map(int , input().split()))

print(sol.getConcatenation(n))
