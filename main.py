class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        element = 0
        summ =[]
        for i in range(0,len(nums)):
            element += nums[i]
            summ.append(element)
        return summ
         
