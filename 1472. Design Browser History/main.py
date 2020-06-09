class BrowserHistory:

    def __init__(self, homepage: str):
        self.q = [homepage]
        self.x = 0

    def visit(self, url: str) -> None:
        self.q = self.q[:self.x+1]
        self.q.append(url)
        self.x += 1

    def back(self, steps: int) -> str:
        steps = min(steps, self.x)
        self.x -= steps
        return self.q[self.x]

    def forward(self, steps: int) -> str:
        steps = min(steps, len(self.q)-self.x-1)
        self.x += steps
        return self.q[self.x]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
