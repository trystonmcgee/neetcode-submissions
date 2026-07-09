class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = []

    def get(self, i: int) -> int:
        if self.array:
            return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if len(self.array) == self.capacity:
            self.resize()

        self.array.append(n)

    def popback(self) -> int:
        if self.array:
            res = self.array.pop()
            return res 

    def resize(self) -> None:
        if self.capacity == 0:
            self.capacity == 1
        else:
            self.capacity *= 2

    def getSize(self) -> int:
        return len(self.array)
    
    def getCapacity(self) -> int:
        return self.capacity