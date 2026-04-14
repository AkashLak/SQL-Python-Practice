class Solution(object):
    def findMin(self, nums):
        """
        Finds the minimum element in a rotated sorted array
        """
        #Initialize result with first element
        res = nums[0]
        #Left and right pointers
        l , r = 0, len(nums) - 1

        while l <= r:
            #If current subarray already sorted, then leftmost element is min
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break
            #get middle element
            m = (l + r) // 2
            res = min(res, nums[m])
            #Check which side is sorted 
            if nums[m] >= nums[l]:
                #left half sorted, so min must be in right half
                l = m + 1
            else:
                #right half sorted, so min must be in left half (includes m)
                r = m - 1
        return res