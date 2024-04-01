class BinaryTreeNode:
    # class constructor
    def __init__(self, key):
        # each node keeps track of three things, key(data), left child and right child
        self.key = key
        self.left = None
        self.right = None
        
    def addChild(self, key):
        # this method adds a new node in the BST
        # if key of the current node is equal to the key that you want to insert
        # then return from the addChild method(as BST can't have duplicate keys)
        if key == self.key:
            return
        # if the key you want to insert into BST is less than the key of the the current node
        # then check if the left child is already there or not
        elif key < self.key: 
            # if self.left is true, it means left child is already there
            # then key will be added as a child to left child
            if self.left: 
                self.left.addChild(key)
            # if self.left is false, it means left child is not added yet
            # now key will added as the left child node
            else:
                self.left = BinaryTreeNode(key)
        else:
            # if self.right is true, it means right child is already there
            # then key will be added as a child to right child            
            if self.right:
                self.right.addChild(key)
            else:
            # if self.right is false, it means right child is not there
            # now key will added as the right child node
                self.right = BinaryTreeNode(key)
                
    def inorderTraversal(self):
        # This method travers the BST according to inorder traversal, adds the traversed node in inorderList
        # and returns the inorderList 
        inorderList = []
        if self.left:
            # if left subtree is there, traverse it according to inorderTraversal
            inorderList =  inorderList+ self.left.inorderTraversal()
        
        # traverse the root node   
        inorderList.append(self.key)
        
        if self.right:
            # if right subtree is there, traverse it according to inorderTraversal
            inorderList += self.right.inorderTraversal()
            
        return inorderList
        
    def preorderTraversal(self):
        # This method travers the BST according to preorder traversal, adds the traversed node in preorderList
        # and returns the preorderList 
        preorderList = []
        
        # traverse the root node   
        preorderList.append(self.key)
        
        if self.left:
            # if left subtree is there, traverse it according to preorderTraversal
            preorderList =  preorderList+ self.left.preorderTraversal()

        
        if self.right:
            # if right subtree is there, traverse it according to preorderTraversal
            preorderList += self.right.preorderTraversal()
        return preorderList 
    
    def postorderTraversal(self):
        # This method travers the BST according to postorder traversal, adds the traversed node in postorderList
        # and returns the postorderList 
        postorderList = []
        
        if self.left:
            # if left subtree is there, traverse it according to postorderTraversal
            postorderList = postorderList+ self.left.postorderTraversal()

        
        if self.right:
            # if right subtree is there, traverse it according to postorderTraversal
            postorderList += self.right.postorderTraversal()
        
        # traverse the root node   
        postorderList.append(self.key)
        return postorderList        
        
    def find_min(self):
        # This method return the value of node containing the minimum key value
        #keep traversing the left child until you find a node with no left child further,
        # else recursively keep going left
        if self.left is None:
            return self.key
        return self.left.find_min()
        
    def find_max(self):
        #This method returns the node value containing the maximum key value
        if self.right is None:
            return self.key
        return self.right.find_max()
        
    def deleteNode(self, val):
        #This method deletes the node with key == val
        # First search to the node you want to delete 
        # if val is less than current node's key, then val might be present in the left subtree
        if val < self.key:
            if self.left: 
                self.left = self.left.deleteNode(val)
        # else if val is greater than current node's key, then val might be present in right subtree
        elif val > self.key:
            if self.right:
                self.right = self.right.deleteNode(val)
        else: # if val is neither greater nor smaller, hence we are at the node we have to delete
            # self.left is None and self.right is None, the node we are deleting is a leaf node
            if self.left is None and self.right is None:
                return None
            # if self.left is None then node we are deleting is node with only right child
            elif self.left is None:
                return self.right
            # if self.right is None then node we are deleting is node with only left child
            elif self.right is None:
                return self.left
            else:
            # if self.right and self.left both are not None, then we are deleting a node with both child nodes 
                #find the in-order successor and copy that in node we want to delete
                min = self.right.find_min() # node with minimum value in right subtree is the inorder successor 
                self.key = min # copying
                self.right = self.right.deleteNode(min) #delete the dulicate node
        return self
    
    def search(self, value):
        # this is boolean method, which returns true, if value is found else returns false
        # if value is equal to the key of the current node, then key is found, return true,
        # else search for it recursively in left subtree and right subtree
        if value == self.key:
            return True
        # if value we are looking for, is smaller than current node's key, 
        # then value might be present in left subtree  
        elif value < self.key:
            if self.left: 
                return self.left.search(value)
            else:
                return False
        # if value we are looking for, is greater than current node's key, 
        # then value might be present in right subtree        
        else: 
            if self.right:
                return self.right.search(value)
            else:
                return False
                
        

def bulidBinarySearchTree(list):
    root = BinaryTreeNode(list[0])
    for i in range(1, len(list)):
        root.addChild(list[i])
    return root

if __name__ == "__main__":
    root = bulidBinarySearchTree([9,8,11,7,3,4,2,19,34])
    print(root.inorderTraversal())
    #root.deleteNode(3)
    print(root.inorderTraversal())
    print(root.find_max())
    print(root.search(7))
    print(root.preorderTraversal())
    print(root.postorderTraversal())
