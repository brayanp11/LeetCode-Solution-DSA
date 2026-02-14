class RecentCounter:

    def __init__(self):
        self.deque = deque()

    def ping(self, t: int) -> int:
        self.deque.append(t)

        limit = t - 3000

        while self.deque and self.deque[0] < limit:
            self.deque.popleft()

        return len(self.deque)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)