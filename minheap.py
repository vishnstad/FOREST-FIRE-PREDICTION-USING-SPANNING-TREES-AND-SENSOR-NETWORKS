class minheap:
    def __init__(self):
        self.heap = []
    
    def insert(self, element):
        self.heap.append(element)
        self.heapify_up(len(self.heap)-1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        self.swap(0,len(self.heap)-1)
        min_elem = self.heap.pop()
        self.heapify_down(0)
        return min_elem
        

    def heapify_up(self, index):
        parent_index = (index-1)//2
        while index != 0 and self.heap[index] < self.heap[parent_index]:
            self.swap(parent_index, index)
            index = parent_index
            parent_index = (index-1)//2

    def heapify_down(self, index):
        smallest = index
        left_index = 2*index+1
        right_index = 2*index+2

        if left_index < len(self.heap) and self.heap[left_index] < self.heap[index]:
            smallest = left_index
        if right_index < len(self.heap) and self.heap[right_index] < self.heap[index]:
            smallest = right_index
        
        if smallest != index:
            self.swap(smallest, index)
            self.heapify_down(smallest)

    def swap(self, parent, child):
        self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]

###############################################
'''
h = minheap()
h.insert(4)
print(h.heap)
h.insert(10)
print(h.heap)
h.insert(7)
print(h.heap)
h.insert(2)
print(h.heap)
h.insert(3)
print(h.heap)


print(h.extract_min())
'''