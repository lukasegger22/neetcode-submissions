class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        half = (len(nums1)+len(nums2)+1)//2
        total_len = len(nums1) + len(nums2)
        left = 0
        right = len(nums1)
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = half - partition1
            L1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            R1 = nums1[partition1] if partition1 < len(nums1) else float('inf')
            
            L2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            R2 = nums2[partition2] if partition2 < len(nums2) else float('inf')
            
            if L1 <= R2 and L2 <= R1:
                
                if total_len % 2 == 1:
                    return float(max(L1, L2))
                
                else:
                    return (max(L1, L2) + min(R1, R2)) / 2.0
                
            elif L1 > R2:
                right = partition1 - 1
            else:
                left = partition1 + 1
                
        return -1.0