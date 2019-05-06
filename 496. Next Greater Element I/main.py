class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        
        for e in nums1:
            m=e
            for i in range(len(nums2)):
                if nums2[i]==e:
                    break
            for j in range(i+1,len(nums2)):
                if nums2[j]>m:
                    m=nums2[j]
                    break
            if m==e:
                res.append(-1)
            else:
                res.append(m)
                
        return res
