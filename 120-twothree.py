def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        2032
        """

        ans1=[x for x in nums1 if x in nums2 or x in nums3]

        ans2=[x for x in nums2 if x in nums3]

        ans1.extend(ans2)

        return set(ans1)