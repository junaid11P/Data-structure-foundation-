class Queue:
  def __init__(self):
    self.queue=[]

	def is_empty(self):
    return len(self.queue)==0
  def is_full(self):
    return self.rear==len(self.queue)
    
  def enqueue(self,item):
  	if self.is_full():
      print("The queue is full")
    else:
    	if self.front==-1:
      	self.front=0
      rear+=1
      self.queue[self.rear]=item

	def dequeue(self):
    if self.is_empty():
      print("The queue is empty")
		else:
			return self.queue[self.front]=-1

	def peek(self):
    if self.is_empty():
      print("The queue is empty")
  else:
		return self.front
        
if __name__=="__main__":
  enqueue(1)
  enqueue(2)
  enqueue(3)
  print("The elements are:",queue.queue)
  dequeue()
  print("The elements are:",queue.queue)
  enqueue(10)
  print("The top most element of queue",queue.peek())
  print("The elements are:",queue.queue)
