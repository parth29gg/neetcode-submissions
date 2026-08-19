class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        n1=len(set(nums))
        return n1!=n;