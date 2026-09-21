class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1

    # pop and return at the element at the end of the array
    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1

        # return the popped element
        return self.arr[self.length]

    # double the capacity of the array
    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity

        # copy the elements into the new array
        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr

    # return number of elements in the array
    def getSize(self) -> int:
        return self.length        
    
    # return capacity of the array
    def getCapacity(self) -> int:
        return self.capacity
