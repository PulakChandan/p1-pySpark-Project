class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def get_top(self):
        return self.__top

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if self.__top== (self.get_max_size()-1):
            return True
        else:
            return False
            
        #Remove pass and write the logic to check whether stack is full. If the stack is full, return true else return false.

    def push(self,data):
        if not self.is_full():
            self.__top=self.__top+1
            self.__elements[self.__top]=data
        else:
            print("the stack is full!")
    
    def display(self):
        for i in range(self.__top,-1,-1):
            print(self.__elements[i])
            
    def is_empty(self):
        if self.__top==-1:
            return True
        else:
            return False
            
    def pop(self):
        if not self.is_empty():
            popped=self.__elements[self.__top+1]
            self.__top=self.__top-1
            return popped
            
        else:
            print("Stack empty!!")
            
        
        #Remove pass and write the logic to push element into the stack. Element should be pushed only if the stack is not full. Otherwise, display appropriate message


stack1=Stack(5)
#Push all the required element(s).
stack1.push("Green")
stack1.push("Red")
stack1.push("Magenta")
stack1.push("Indigo")
stack1.display()
print(stack1.pop(),"popped out!")
print(stack1.pop(),"popped out!")
print(stack1.pop(),"popped out!")
print(stack1.pop(),"popped out!")
print(stack1.pop(),"popped out!")
stack1.display()

  