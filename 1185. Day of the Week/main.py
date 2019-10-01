class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        res = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        k = day
        m = (month + 9) % 12 + 1
        if month == 1 or month == 2: year = year - 1
        D = year % 100
        C = year // 100
        f = k + ((13*m-1)//5) + D + (D//4) + (C//4) - 2*C
        f = f%7
        return res[f]
