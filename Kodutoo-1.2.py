# LIFO/FIFO andmestruktuur

class Stack:
    def __init__(self):
        self.items = [] # loob tühja listi
    
    def push(self, item):
        self.items.append(item) # lisab elemendi listi lõppu
    
    def pop(self):
        if not self.is_empty(): # kui list ei ole tühi
            return self.items.pop() # eemaldab ja tagastab elemendi listi lõpust
        return None
    
    def is_empty(self):
        return len(self.items) == 0 # tagastab True, kui list on tühi
    
    def size(self):
        return len(self.items) # tagastab listi pikkuse

# Kogu LIFO ajaline keerukus on O(1), kuna elemendi lisamine ja eemaldamine toimub listi lõpus ja listi pikkus ei mõjuta ajalise keerukuse suurust.
# Iga funktsiooni ajaline keerukus on O(1).