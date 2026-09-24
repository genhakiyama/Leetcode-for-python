class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_set = set(nums)
        if len(nums_set) == len(nums) :
            return False

        return True 

arr = list(map(int , input().split()))
print(Solution().containsDuplicate(arr))