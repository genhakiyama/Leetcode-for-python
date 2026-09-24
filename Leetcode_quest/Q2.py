class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result = []
        for x , y in zip(nums[:n] , nums[n:]) :
            result.append(x)
            result.append(y)

        return result

sol = Solution()
arr = list(map(int , input().split()))
n = int(input())

print(sol.shuffle(arr,n))


