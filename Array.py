class Data:
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def display(self):
        print("Array elements are:")
        for element in self.data[:self.size]:
            print(element, end=" ")
        print()

    def insert(self, index, value):
        if self.size == self.capacity:
            print("Array Overflow. Resizing...")
            self.resize(self.capacity * 2)

        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = value
        self.size += 1

    def delete(self, index):
        if self.size == 0:
            print("Array Underflow")
            return

        deleted_element = self.data[index]
        self.data[index] = None

        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.size -= 1

    def search_by_value(self, value):
        if value in self.data[:self.size]:
            index = self.data.index(value)
            print("Element", value, "found at index", index)
        else:
            print("Element", value, "not found in the data.")

    def update(self, index, new_value):
        if 0 <= index < self.size:
            old_value = self.data[index]
            self.data[index] = new_value
            print("Element at index", index, "updated from", old_value, "to", new_value)
        else:
            print("Invalid index for update.")

    def resize(self, new_capacity):
        self.capacity = new_capacity
        self.data = self.data[:self.size] + [None] * (new_capacity - self.size)

if __name__ == "__main__":

    a1 = Data(10)
    a1.display()
    a1.insert(0, 20)
    a1.insert(1, 30)
    a1.insert(2, 40)
    a1.insert(3, 50)
    a1.display()
    a1.insert(2, 100)
    a1.delete(1)
    a1.display()

    a1.search_by_value(20)
    a1.update(0, 8)
    a1.display()
