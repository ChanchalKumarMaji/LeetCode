class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.counter = 0
        self.dict = {}
        for i in range(len(products)):
            self.dict[products[i]] = prices[i]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.counter += 1
        res = 0
        for i in range(len(product)):
            res += self.dict[product[i]] * amount[i]
        if self.counter == self.n:
            self.counter = 0
            res -= self.discount * res / 100
        return res


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
