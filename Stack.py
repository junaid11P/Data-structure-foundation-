class Stack:
  def __init__(self):
    self.stack=[]

  def is_empty(self):
    return len(self.stack) == 0

  def push(self, item):
    self.stack.append(item)

  def pop(self):
    if self.is_empty():
      print("Stack is empty. Cannot pop.")
    else:
      return self.stack.pop()
            
  def peek(self):
    if self.is_empty():
      print("Stack is empty. Cannot peek.")
    else:
      return self.stack[-1]

  def size(self):
    return len(self.stack)

if __name__=='__main__':
  stack=Stack()
  stack.push(1);
  stack.push(2);
  stack.push(3);
  print("The elements are:",stack.stack)
  stack.pop()
  print("The elements are:",stack.stack)
  print("The top most element in the stack:",stack.peek())
  print("The size of the stack:",stack.size())
      
