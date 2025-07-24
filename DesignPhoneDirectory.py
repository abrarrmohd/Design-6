class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.availableSet = set()
        self.availableQ = collections.deque()
        for i in range(maxNumbers):
            self.availableQ.append(i)
            self.availableSet.add(i)

    def get(self) -> int:
        if len(self.availableQ) == 0:
            return -1
        number = self.availableQ.popleft()
        self.availableSet.remove(number)
        return number
        

    def check(self, number: int) -> bool:
        if number in self.availableSet:
            return True
        return False
        

    def release(self, number: int) -> None:
        if number in self.availableSet:
            return

        self.availableQ.append(number)
        self.availableSet.add(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)