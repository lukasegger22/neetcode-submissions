class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = nums1 + nums2
        merge.sort()
        if len(merge) % 2 == 1:
            return float(merge[(len(merge)-1)//2])
        else:
            index = (len(merge)-1) // 2
            return float((merge[index] + merge[index+1]) /2)