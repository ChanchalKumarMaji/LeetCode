class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = 0.5 * (hour * 60 + minutes)
        minutes_angle = 6 * minutes
        angle = abs(hour_angle - minutes_angle)
        angle = min(angle, 360 - angle)
        return angle
