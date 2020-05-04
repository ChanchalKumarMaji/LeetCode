class UndergroundSystem:

    def __init__(self):
        self.id_in = {}
        self.d = {}
        self.c = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id_in[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        a, b = self.id_in[id]
        if (b, stationName) not in self.d:
            self.d[(b, stationName)] = t - a
            self.c[(b, stationName)] = 1
        else:
            self.d[(b, stationName)] += t - a
            self.c[(b, stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.d[(startStation, endStation)] / self.c[(startStation, endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
