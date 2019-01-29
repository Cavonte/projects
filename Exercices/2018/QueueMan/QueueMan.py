class QueueMine(list):
    MAX_SIZE = 3

    def enqueue(self,item):
        return len(self)+1 <= self.MAX_SIZE and self.append(item) or False
    def dequeue(self):
        return not self.isEmpty() and self.pop(0) or None

    def peek(self):
        return not self.isEmpty() and  self[0] or None

    def isEmpty(self):
        return not bool(self)

    def isFull(self):
        return self.MAX_SIZE == len(self)

    def append(self,item):
        return None

    # override behavior of list to maintain encapsulation
    def insert(self,i,x):
        return
    def remove(self,item):
        return
    def pop(self,index):
        return

    def index(self,item):
        return

    def sort(self,cmp=None,key=None,reverse=None):
        return



queue = QueueMine()
print(queue)
print(queue.isEmpty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.enqueue(4))
print(queue.isFull())
print(queue)
print(queue.peek())
print(queue)
print(queue.dequeue())
print(queue)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.peek())
