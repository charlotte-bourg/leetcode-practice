class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1Copy = nums1[:m]
        pn2, pn1c = 0, 0 # read pointers (from nums2 and nums1 copy)
        for pn1 in range(m + n): # write pointer (into nums1 in place)
            if pn2 >= n or (pn1c < m and nums1Copy[pn1c] <= nums2[pn2]):
                nums1[pn1] = nums1Copy[pn1c]
                pn1c += 1 
            else:
                nums1[pn1] = nums2[pn2]
                pn2 += 1

        

# merge nums2 into nums1

