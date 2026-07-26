class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = 0
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        right = len(nums1)

        while left <= right:
            half = (len(nums1) + len(nums2))//2
            partition1 = (left+right)//2
            partition2 = half - partition1
            L1 = nums1[partition1 - 1] if partition1 > 0 else float("-inf")
            L2 = nums2[partition2 - 1] if partition2 > 0 else float("-inf")
            R1 = nums1[partition1] if partition1 < len(nums1) else float("inf")
            R2 = nums2[partition2] if partition2 < len(nums2) else float("inf")
            if L1 <= R2 and L2 <= R1:
                if (len(nums1)+len(nums2)) % 2 == 0:
                    return (max(L1, L2) + min(R1, R2)) / 2
                else:
                    return min(R1, R2)
            elif L1 > R2 and L2 < R1:
                right = partition1-1
            else:
                left =partition1+1
        return -1
