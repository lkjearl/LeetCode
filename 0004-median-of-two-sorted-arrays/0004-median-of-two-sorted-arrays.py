class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) %2 == 0:
            a = nums1[len(nums1)//2]
            b = nums1[(len(nums1)//2) -1]
            return float((a+b)/2)
        else:
            return float(nums1[(len(nums1)-1)//2])