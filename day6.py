#day 6
# 643. Maximum Average Subarray I

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sums = sum(nums[:k])
        maxsums = sums
        for i in range(len(nums)-k):
            sums -= nums[i]
            sums += nums[i+k]
            maxsums = max(maxsums, sums)
        return maxsums / float(k) 
