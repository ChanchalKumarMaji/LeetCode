class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort()
        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()
        a, b = 0, 0
        for i in range(1, len(horizontalCuts)):
            a = max(a, horizontalCuts[i]-horizontalCuts[i-1])
        for i in range(1, len(verticalCuts)):
            b = max(b, verticalCuts[i]-verticalCuts[i-1])
        return (a*b) % (10**9 + 7)
