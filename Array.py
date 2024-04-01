class Array:
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def insertAtLast(self, element):
        if self.size == self.capacity:
            print("Array Overflow")
            return
        self.data[self.size] = element
        self.size += 1

    def insert_in_between(self, index, element):
        if self.size == self.capacity:
            print("Array Overflow")
            return
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = element
        self.size += 1

    def insertAtFirst(self, element):
        self.insert_in_between(0, element)

    def deleteAtLast(self):
        if self.size == 0:
            print("Array Underflow/empty, delete can't be performed")
            return
        deletedValue = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1
        return deletedValue

    def delete_at_given_index(self, index):
        if self.size == 0 or (index < 0 or index > self.size - 1):
            print("Array is empty or given index is invalid")
            return
        deletedValue = self.data[index]
        for i in range(index, self.size):
            self.data[i] = self.data[i + 1]
        self.size -= 1
        return deletedValue

    def deleteAtHead(self):
        return self.delete_at_given_index(0)


if __name__ == "__main__":
    array1 = Array(15)
    array2 = Array(15)
    print(array1.data)
    array1.insertAtLast(15)
    array1.insertAtLast(21)
    array1.insertAtLast(10)
    array1.insert_in_between(1, 34)
    array1.insertAtFirst(56)
    print(array1.data)
    print("deleted value is: ", array1.deleteAtLast())
    print("Deleted value is: ", array1.delete_at_given_index(1))
    print("Deleted value is: ", array1.deleteAtHead())
    print(array1.data)
