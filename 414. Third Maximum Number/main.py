class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one=two=three=-100000000000
        for num in nums:
            if num>one:
                one,two,three=num,one,two
            elif num<one and num>two:
                two,three=num,two 
            elif num<two and num>three:
                three=num 
                
        if three!=-100000000000:
            return three
        return one
