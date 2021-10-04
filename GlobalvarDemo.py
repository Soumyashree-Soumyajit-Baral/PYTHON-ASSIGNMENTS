x='python'
def display():
    #global x
    x='java'
    print('B global x value inside the function',globals()['x'])
    print('B Inside display function :',x)
    globals()['x']='julia'
    print('A global x value inside the function',globals()['x'])

    print('A Inside display function :',x)

    #x='python'
    #print('Inside display function :',x)
class A:
    def show(self):
        print('Inside the class and show method :',x)

a1=A()
a1.show()
display()
print('outside the function :',x)
#global vs globals()-----interview q
