class Book:
    def __init__(self,a,price):
        self.pages=a
        self.price=price
    def __str__(self):
        print('Inside str method')
        #print(str(type(self))+' Object at ' +hex(id(self)))
        #print(self.__module__+' Object at ' +hex(id(self)))
        
        return('This object is Book Class and it has %d of pages and cost is %d'%(self.pages,self.price))
    def __add__(self,other):
        print('Inside Add Method')
        return Book(self.pages+other.pages,self.price+other.price)

    def display(self):
        #print(self.__module__+' Object at ' +hex(id(self)))
        print('No. of pages in the book',self.pages)


b1=Book(100,400)
b2=Book(385,450)
b3=Book(500,550)
print(type(b1),b1)
print(id(b1),hex(id(b1)))
print(type(b2),b2)
print(id(b2),hex(id(b2)))
#b4=b1.pages+b2.pages
b4=b1+b2+b3
print(type(b4),b4)
#b1.display()
#b2.display()
