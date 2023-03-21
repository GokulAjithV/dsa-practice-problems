class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        dummy = []
        
        for i in nums1:
            if i in nums2:
                if i not in dummy :
                    result.append(i)
                    dummy.append(i)
        return result             