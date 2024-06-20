
#Day4 - leetcode 1004. Max Consecutive Ones III
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        maxi = 0
        zc = 0
        for r in range(len(nums)):
            if nums[r]==0:
                zc+=1
            
            if zc>k:
                if nums[l]==0:
                    zc-=1
                l+=1
            maxi = max(maxi, r-l+1)
        return maxi
