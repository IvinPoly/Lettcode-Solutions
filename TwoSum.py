class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map={}
        for i,n in enumerate(nums):
            x=target-n

            if x in num_map:
                return[num_map[x],i]
            num_map[n]=i
        return
