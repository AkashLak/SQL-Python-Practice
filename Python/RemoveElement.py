class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        correct_counter = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[correct_counter] = nums[i]
                correct_counter = correct_counter + 1
        return correct_counter
