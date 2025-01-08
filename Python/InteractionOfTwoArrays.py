class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        unique_items = []
        for i in nums1:
            if i in nums2 and i not in unique_items:
                unique_items.append(i)

        return unique_items
