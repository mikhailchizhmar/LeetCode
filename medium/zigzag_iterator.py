# https://leetcode.com/problems/zigzag-iterator

class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.i = self.j = 0
        cond = len(v1) > 0
        self.from_v1 = cond
        self.from_v2 = not cond

    """
    @return: An integer
    """
    def _next(self):
        if self.hasNext():
            if self.from_v1:
                cond = self.j < len(self.v2)
                self.from_v1 = not cond
                self.from_v2 = cond
                self.i += 1
                return self.v1[self.i - 1]
            else:
                cond = self.i < len(self.v1)
                self.from_v1 = cond
                self.from_v2 = not cond
                self.j += 1
                return self.v2[self.j - 1]
        else:
            raise StopIteration

    """
    @return: True if has next
    """
    def hasNext(self):
        return self.i < len(self.v1) or self.j < len(self.v2)


solution, result = ZigzagIterator([1, 2], [3, 4, 5, 6]), []
while solution.hasNext():
    result.append(solution._next())
assert result == [1, 3, 2, 4, 5, 6]

solution, result = ZigzagIterator([1, 1, 1, 1], [3, 4, 5, 6]), []
while solution.hasNext():
    result.append(solution._next())
assert result == [1, 3, 1, 4, 1, 5, 1, 6]

solution, result = ZigzagIterator([], [11]), []
while solution.hasNext():
    result.append(solution._next())
assert result == [11]

solution, result = ZigzagIterator([], []), []
while solution.hasNext():
    result.append(solution._next())
assert result == []
