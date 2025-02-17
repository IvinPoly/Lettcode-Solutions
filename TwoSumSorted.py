class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[]
        l,r=0,len(numbers)-1
        for i in range(len(numbers)):
            if numbers[l]+numbers[r]==target:
                res.append(l+1)
                res.append(r+1)
                break
            elif numbers[l]+numbers[r]<target:
                l+=1
            else:
                r-=1
        return res
