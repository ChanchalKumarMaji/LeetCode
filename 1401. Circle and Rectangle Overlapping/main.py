class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x, y = (x1+x2) / 2, (y1+y2) / 2
        cdx, cdy = abs(x_center-x), abs(y_center-y)
        rw, rh = (x2-x1) / 2, (y2-y1) / 2
        if cdx > (rw + radius):
            return False
        if cdy > (rh + radius):
            return False
        if cdx <= rw:
            return True
        if cdy <= rh:
            return True
        cds = (cdx - rw) ** 2 + (cdy - rh) ** 2
        return cds <= radius ** 2
