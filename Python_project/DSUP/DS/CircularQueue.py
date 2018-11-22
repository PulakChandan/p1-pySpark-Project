
class CircularQueue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=-1
    def get_front(self):
        return self.__front
    
    def get_rear(self):
        return self.__rear
    
    def get_max_size(self):
        return self.__max_size
    
    def is_full(self):
        if (self.__front==0 and self.__rear==self.__max_size-1) or (self.__front==self.__rear+1):
            return True
        else:
            return False
    def is_empty(self):
        if (self.__front==-1 and self.__rear==-1):
            return True
        else:
            return False
        
    def enqueue(self,data):
        if not self.is_full():
            
            if self.is_empty():
                self.__front=self.__rear=0
                
            elif self.__rear == (self.__max_size-1):
                self.__rear=0
                
            else:
                self.__rear+=1
                
            self.__elements[self.__rear]=data
        else:
            print("Queue full !!")
            
    def dequeue(self):
        if not self.is_empty():
            data=self.__elements[self.__front]
            #last element condition
            if self.__rear == self.__front:   
                self.__rear= -1
                self.__front= -1
                
            elif self.__front==(self.__max_size-1):
                self.__front=0
                
            else:
                self.__front+=1  
            return data
        else:
            print("Queue empty")
            return None
        
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            
            
        else:
            if self.__front <= self.__rear:
                for i in range(self.__front,self.__rear+1):
                    print(self.__elements[i])
                    
            else:
                for i in range(self.__front,self.__max_size):
                    print(self.__elements[i])
                    
                for i in range(0,self.__rear+1):
                    print(self.__elements[i])
                
cq1=CircularQueue(3)
cq1.enqueue("Mysuru")   
cq1.enqueue("Bhubaneswar") 
print(cq1.dequeue() ,"removed") 
cq1.enqueue("Sydney") 
cq1.enqueue("Bhopal") 
print(cq1.dequeue() ,"removed") 
print(cq1.dequeue() ,"removed") 
cq1.enqueue("Chennai") 
print(cq1.dequeue() ,"removed") 
cq1.display()
            
            
            
            
        
        