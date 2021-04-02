import numpy as np

class Queue:
    def __init__(self):
        self.q = []
    
    def enqueue(self, x):
        self.q.append(x)
    
    def dequeue(self):
        return self.q.pop(0)
    
    def empty(self):
        return len(self.q) == 0
    
    def size(self):
        return len(self.q)
        
    # def __init__(self, size):
    #     self.size = size
    #     self.q = np.zeros(size, dtype = int)
    #     self.ptr = 0 
    #     self.empty = True
    #     self.full = False
    
    # def enqueue(self, x):
    #     if not self.full:
    #         self.q[self.ptr] = x
    #         self.ptr += 1
    #         self.empty = False
    #         if self.ptr == self.size:
    #             self.full = True
    #             self.ptr -= 1
    #     else:
    #         print("{0} cannot be added to Q full".format(x))
    
    # def dequeue(self):
    #     if not self.empty:
    #         front = self.q[0]
    #         self.ptr -= 1
    #         self.full = False
    #         if self.ptr == -1:
    #             self.empty = True
    #             self.ptr = 0
    #         else:
    #             for i in range(1, self.size):
    #                 self.q[i-1] = self.q[i]
    #         return front
    #     else:
    #         return "Q is empty"
    
    # def empty(self):
    #     return self.empty
    
    # def size(self):
    #     return len(self.q)
    
    # def __str__(self):
    #     return self.q