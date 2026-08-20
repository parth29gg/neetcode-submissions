class Solution:
    def f(self, idx:int, nums:List[int], dp:List[int])->int:
        n=len(nums)
        if idx >= n :
            return 0
        if dp[idx]!=-1:
            return dp[idx]
        take=nums[idx]+self.f(idx+2,nums,dp)
        nottake=self.f(idx+1,nums,dp)
        dp[idx]=max(take,nottake)
        return dp[idx]

    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*(n);

        return self.f(0,nums,dp);
        