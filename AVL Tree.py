class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert_node(self, root, value):
        if not root:
            return AVLNode(value)
        
        if value < root.value:
            root.left = self.insert_node(root.left, value)
        else:
            root.right = self.insert_node(root.right, value)

        root.height = 1 + max(self.avl_height(root.left), self.avl_height(root.right))

        balance_factor = self.avl_balance_factor(root)

        if balance_factor > 1:
            if value < root.left.value:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance_factor < -1:
            if value > root.right.value:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def avl_height(self, root): 
        return root.height if root else 0

    def avl_balance_factor(self, root):
        return self.avl_height(root.left) - self.avl_height(root.right) if root else 0

    def avl_min_value(self, root):
        return root if root is None or root.left is None else self.avl_min_value(root.left)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print("Node", root.value, "Height =", self.avl_balance_factor(root))
            self.inorder_traversal(root.right)

    def left_rotate(self, b):
        a = b.right
        T2 = a.left
        a.left = b
        b.right = T2
        b.height = 1 + max(self.avl_height(b.left), self.avl_height(b.right))
        a.height = 1 + max(self.avl_height(a.left), self.avl_height(a.right))
        return a

    def right_rotate(self, b):
        a = b.left
        T3 = a.right
        a.right = b
        b.left = T3
        b.height = 1 + max(self.avl_height(b.left), self.avl_height(b.right))
        a.height = 1 + max(self.avl_height(a.left), self.avl_height(a.right))
        return a

    def delete_node(self, root, value):
        if not root:
            return root

        if value < root.value:
            root.left = self.delete_node(root.left, value)
        elif value > root.value:
            root.right = self.delete_node(root.right, value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.avl_min_value(root.right)
            root.value = temp.value
            root.right = self.delete_node(root.right, temp.value)

        if root is None:
            return root

        root.height = 1 + max(self.avl_height(root.left), self.avl_height(root.right))
        balance_factor = self.avl_balance_factor(root)

        if balance_factor > 1:
            if self.avl_balance_factor(root.left) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance_factor < -1:
            if self.avl_balance_factor(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root


# Example usage:
tree = AVLTree()
root_node = None

root_node = tree.insert_node(root_node, 40)
root_node = tree.insert_node(root_node, 70)
root_node = tree.insert_node(root_node, 60)
root_node = tree.insert_node(root_node, 50)
root_node = tree.insert_node(root_node, 100)

print("Inorder Traversal:")
tree.inorder_traversal(root_node)

root_node = tree.delete_node(root_node, 100)
print("\nInorder Traversal After Deletion:")
tree.inorder_traversal(root_node)
