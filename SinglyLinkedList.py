
class SinglyLinkedList:
    def __init__(self):
        self.__list = list()
        
    def add(self,element):
        self.__element = element
        self.__list.append(self.__element)
        
    
    def display(self):
        if len(self.__list) == 0:
            print('List is Empty!')       
        else:
            print("List is:",end=' ')
            for i in self.__list:
                print(i,end=' ')
        print()
                
    
    def delete(self,e):
        self.__e = e
        if e not in self.__list:
            print(f'{self.__e} is Not in List')
            
        else:
            self.__list.remove(self.__e)
        
    
    def clear(self):
        self.__list.clear()
        
    
    def insert(self,ind,val):
        self.__ind = ind
        self.__val = val
        if self.__ind > len(self.__list):
            print()
            print(f'Choose index with in the list length! LIST LENGHT: {len(self.__list)}')
        else:
            self.__list.insert(self.__ind, self.__val)
        print('----------')
        

L = SinglyLinkedList()
L.add(20)
L.add(30)
L.display()

        
        