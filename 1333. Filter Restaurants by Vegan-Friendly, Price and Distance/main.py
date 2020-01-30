class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        res = []
        for restaurant in restaurants:
            i, r, v, p, d = restaurant
            if veganFriendly == 1:
                if v == 1 and p <= maxPrice and d <= maxDistance:
                    res.append([i, r])
            else:
                if p <= maxPrice and d <= maxDistance:
                    res.append([i, r])
        res.sort(key = lambda x : (-x[1], -x[0]))
        return [e[0] for e in res]
