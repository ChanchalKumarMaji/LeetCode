class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        hand.sort()
        while hand:
            #hand.sort()
            try:
                base = hand[0]
                for i in range(W):
                    hand.remove(base+i)
            except:
                return False
            
        return True
