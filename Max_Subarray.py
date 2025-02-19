class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float(-inf)
        cur_sum=0
        n=len(nums)
        for i in range(n):
            cur_sum+=nums[i]
            max_sum=max(max_sum,cur_sum)
            if cur_sum < 0:
                cur_sum=0
        return max_sum
