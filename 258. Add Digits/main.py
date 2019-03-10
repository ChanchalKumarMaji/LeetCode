class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while True:
            if num<10:
                return num
            else:
                num=sum([int(i) for i in str(num)])
