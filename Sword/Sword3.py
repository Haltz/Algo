class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            else:
                return i
            