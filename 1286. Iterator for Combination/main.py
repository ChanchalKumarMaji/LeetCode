class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.res = []
        self.backtrack([], 0, len(characters), combinationLength, characters)
        self.it = 0
        
    def backtrack(self, temp, start, end, k, characters):
        if len(temp) == k: 
            self.res.append(''.join(temp))
        else:
            for i in range(start, end):
                temp.append(characters[i])
                self.backtrack(temp, i+1, end, k, characters)
                temp.pop()

    def next(self) -> str:
        t = self.res[self.it]
        self.it += 1
        return t

    def hasNext(self) -> bool:
        return self.it < len(self.res)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
