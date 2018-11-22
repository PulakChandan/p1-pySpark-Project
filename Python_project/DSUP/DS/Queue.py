              
 
class Queue:
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
        if self.__rear==(self.__max_size-1):
            return True
        else:
            return False
            
    def is_empty(self):
        if (self.__front == -1 and self.__rear == -1):
            return True
        else:
            return False
        
        #Remove pass and write the logic to check whether Queue is full. If the queue is full, return true else return false.
    
    def enqueue(self,data):
        if not self.is_full():
            if self.is_empty():
                self.__rear=self.__front=0
            else:    
                self.__rear=self.__rear+1
            self.__elements[self.__rear]=data
        else:
            print("Queue is full!!")
            
    def dequeue(self):
        if not self.is_empty():
            data=self.__elements[self.__front]
            if self.__front==self.__rear:
                self.__front=self.__rear=-1
            else:
                self.__front=self.__front+1
            return data
        else:
            print("Queue empty!!")
            
        #Remove pass and write the logic to enqueue an element. Enqueue should be done only if queue is not full. Otherwise display appropriate message.
    
    def display(self):
        if not self.is_empty():
            for i in  range(self.__front,self.__rear+1,1):
                print(self.__elements[i])
        #Remove pass and write the logic to display all the queue element(s).

queue1=Queue(3)
#Enqueue all the required element(s).
queue1.enqueue("Tom")
queue1.enqueue("Jack")
queue1.display()
queue1.dequeue()
queue1.dequeue()
print()
queue1.enqueue("Helena")
queue1.enqueue("Harry")
queue1.enqueue("Ram")
queue1.enqueue("Raj")
#queue1.display()
queue1.display()
#Display all the elements in the queue.