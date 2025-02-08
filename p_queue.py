from minheap import minheap
class pqueue():

    def __init__(self):
        self.queue = minheap()
        
    def push(self, item, priority):
        self.queue.insert((priority,item))
    
    def pop(self):
        if len(self.queue.heap) != 0:
            return self.queue.extract_min() # only item needed
        return None
"""     
pq = pqueue()
for i in range(5):
    pq.push(i,1+1)
print(pq.queue.heap)
"""