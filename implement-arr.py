class MyArray() :

    def __init__(self):
        self.length = 0
        self.data = {}
        
    def get(self, index) :
        return self.data[index]
    
    def push(self, item) :
        
        self.data[self.length] = item
        self.length = self.length + 1
    
    def pop(self) :
        if(self.length > 0) :
            item = self.data[self.length - 1]
            del self.data[self.length-1]
            self.length = self.length - 1
            return item
        else :
            return None
    
    def pop_at(self, index) :
        if(self.length > 0 and (index >= 0 and index < self.length) ) :
            item = self.data[index]
            self.shiftItems(index)
            return item

    def shiftItems(self, index):
        for i in range(index, self.length -1) :
            self.data[i] = self.data[i+1]
        del self.data[self.length -1]
        self.length -= 1
            

                
    
    def __str__(self):
        return str(self.__dict__)
        


arr = MyArray()

arr.push(4)
arr.push(5)
arr.push(6)
print(arr.data[1])
print(arr)
arr.pop_at(10)
print(arr)
        
    
        
        
    
        
    
    

