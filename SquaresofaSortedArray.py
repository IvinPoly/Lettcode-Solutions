class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left,right=0,len(nums)-1
        result=[]

        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                result.append(abs(nums[left]**2))
                left+=1
            else:
                result.append(abs(nums[right]**2))
                right -=1
        return result[::-1]
