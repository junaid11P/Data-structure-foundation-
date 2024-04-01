class Linkedlist:
    class Node:
        def __init__(self,data=None,next=None):
            self.data=data
            self.next=next
    def __init__(self):
        self.head=None
        self.size=0
    def insertAtHead(self,element):
        newNode=self.Node(element,self.head)
        if newNode==None:
            print("couldn't create a new node")
            return
        self.head=newNode
        self.size+=1
        
    def insert_in_between(self,element,previousNodeValue):
        newNode=self.Node(element)
        if newNode==None:
            print("couldn't create a new node")
            return
        currentNode=self.head
        while currentNode:
            if currentNode.data==previousNodeValue:
                previousNode=currentNode
                break
            else:
                previousNode=currentNode
                currentNode=currentNode.next
                
        newNode.next=previousNode.next
        previousNode.next=newNode
        self.size+=1
        
    def insertAtTail(self,element):
        newNode=self.Node(element)
        if newNode==None:
            print("couldn't create a new node")
            return
        currentNode=self.head
        while currentNode:
            if currentNode.next==None:
                tailNode=currentNode
                break
            else:
                tail=currentNode
                currentNode=currentNode.next
        tail.next=newNode
        self.size+=1
        
    def deleteAtHead(self):
        if self.size==0:
            print("Linkedlist is empty,delete operation cannot be performed!!")
            return
        deletedValue=self.head.data
        self.head=self.head.next
        self.size-=1
        return deletedValue
        
    def delete_in_between(self):
        if self.size==0:
            print("Linkedlist is empty")
            return
        currentNode=self.head
        previousNode=None
        while currentNode:
            if currentNode.data==element:
                break
            else:
                previousNode=currentNode
                currentNode=currentNode.next
        if previousNode!=None:
            previousNode.next=currentNode.next
            return
        else:
            print("Either the given value is not present in the linked list or it is the head node")
            return
        return currentNode.data
        
    def deleteAtTail(self):
        if self.size==0:
            print("Linkedlist is empty")
            return
        currentNode=self.head
        previousNode=None
        while currentNode.next:
            previousNode=currentNode
            currentNode=currentNode.next
        deletedValue=currentNode.data
        
        if previousNode:
            previousNode.next=None
            return
        else:
            self.head=None
        self.size-=1
        return deletedValue
        
    def traverseLinkedlist(self):
        currentNode=self.head
        while currentNode:
            print(currentNode.data)
            currentNode=currentNode.next

if __name__=="__main__":
    l1=Linkedlist()
    l1.deleteAtHead()
    l1.insertAtHead(23)
    l1.insertAtHead(45)
    l1.insert_in_between(81,45)
    l1.insert_in_between(89,42)
    l1.insertAtTail(90)
    print("Deleted value is:",l1.deleteAtTail())
    l1.delete_in_between(23)
    l1.traverseLinkedlist()
        
