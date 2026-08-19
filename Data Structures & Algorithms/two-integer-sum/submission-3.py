class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums2 = []
        for i in range(n):
            nums2.append((nums[i], i))

        nums2 = sorted(nums2)
        l, r = 0, n - 1
        while l < r:
            s = nums2[l][0] + nums2[r][0]
            if s == target:
                return sorted([nums2[l][1], nums2[r][1]])
            elif s < target:
                l += 1
            else:
                r -= 1
        return [-1, -1]