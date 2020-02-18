from collections import defaultdict

class TweetCounts:

    def __init__(self):
        self.tweetCounts = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweetCounts[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == "minute":
            delta = 60
        elif freq == "hour":
            delta = 3600
        elif freq == "day":
            delta = 86400
        time_list = self.tweetCounts[tweetName]
        n = (endTime - startTime) // delta + 1
        res = [0] * n
        for time in time_list:
            if startTime <= time <= endTime:
                res[(time - startTime) // delta] += 1
        return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
