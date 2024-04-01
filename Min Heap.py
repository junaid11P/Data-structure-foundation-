class MinHeap:
    def __init__(self, capacity):
        # Constructor initializes a fixed capacity, storing 0 in all array elements
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def getParentIndex(self, index):
        return (index - 1) // 2

    def getLeftChildIndex(self, index):
        return 2 * index + 1

    def getRightChildIndex(self, index):
        return 2 * index + 2

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size

    def parent(self, index):
        return self.storage[self.getParentIndex(index)]

    def leftChild(self, index):
        return self.storage[self.getLeftChildIndex(index)]

    def rightChild(self, index):
        return self.storage[self.getRightChildIndex(index)]

    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        # Swap values at given indices
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]

    def insert(self, data):
        # Add a new node to MinHeap
        if self.isFull():
            raise Exception("Heap is Full")
        
        # Add data as the last element in the storage list
        self.storage[self.size] = data
        self.size += 1
        
        # Maintain MinHeap property by calling heapifyUp
        self.heapifyUp()

    def heapifyUp(self):
        index = self.size - 1
        
        # Swap values with parent as long as the heap property is violated
        while self.hasParent(index) and self.parent(index) > self.storage[index]:
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)

    def removeMin(self):
        # Delete the minimum value (root node) from MinHeap
        if self.size == 0:
            raise Exception("Empty Heap")
        
        # Assign root node value to data for later return
        data = self.storage[0]
        
        # Replace root with the last node and update size
        self.storage[0] = self.storage[self.size - 1]
        self.storage[self.size - 1] = 0
        self.size -= 1
        
        # Maintain MinHeap property by calling heapifyDown
        self.heapifyDown()
        
        return data

    def heapifyDown(self):
        index = 0
        
        # Continue until the heap property is satisfied
        while self.hasLeftChild(index):
            smallerChildIndex = self.getLeftChildIndex(index)
            
            # If right child is smaller, update the smallerChildIndex
            if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index):
                smallerChildIndex = self.getRightChildIndex(index)
            
            # If current node is smaller than its smallest child, break out
            if self.storage[index] < self.storage[smallerChildIndex]:
                break
            else:
                # Swap current node with its smallest child
                self.swap(index, smallerChildIndex)
                index = smallerChildIndex

if __name__ == "__main__":
    minH = MinHeap(7)
    minH.insert(10)
    minH.insert(20)
    minH.insert(5)
    minH.insert(2)
    print(minH.storage)
