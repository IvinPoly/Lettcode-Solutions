class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        s=set()
        for v in counter.values():
            if v in s:
                return False
            else:
                s.add(v)
        return True

