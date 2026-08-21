class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(nums)):
            mp[nums[i]]+=1
        sorted_keys = sorted(mp, key=lambda key: mp[key])  # ascending by frequency

        n2 = len(mp)
        ans = []
        cnt = 0
        for key in sorted_keys:
            cnt += 1
            if cnt <= n2 - k:
                continue
            else:
                ans.append(key)
        return ans