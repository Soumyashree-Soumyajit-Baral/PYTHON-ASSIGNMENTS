"""
Diff between Iterable and Iterator...

Generator is a function that returns an object (iterator) which we can iterate
over (one value at a time).

Generator functions allow you to declare a function that behaves like
an iterator, i.e. it can be used in a for loop.

The generator yields one item at a time and generates item only when in demand.
Whereas, in a list comprehension, Python reserves memory for the whole list.
Thus we can say that the generator expressions are memory efficient than
the lists

How to create Generator function in python..
1. defining a normal function, but with a yield statement instead of a return statement.
2. If a function contains at least one yield statement (it may contain other yield or return
   statements), it becomes a generator function.
   Both yield and return will return some value from a function.
3. The difference is return statement terminates a function entirely,
   yield statement pauses the function saving all its states and
   later continues from there on successive calls.

"""
#simple generator function
def gen1():
    i = 1
    print('1st Print')
    # Generator function contains yield statements
    yield i

    i += 1
    print('2nd Print')
    yield i

    i += 1
    print('3rd Print')
    yield i
    return 5

for j in gen1():
    print(j)

#a = gen1()  #calling ur function
#print(a,type(a))
#next(a)  #yield
#print()  #
#next(a)  #yield
#print()
#next(a)  #yield
#print()
#next(a)  #comment this line later



"""
The major difference between a list comprehension and a generator expression is that
a list comprehension produces the entire list while the generator expression produces
one item at a time (Due to this,a generator expression is much more memory efficient than
an equivalent list comprehension).


my_list = [1, 3, 6, 10]

# square each term using list comprehension
list_ = [x**2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x**2 for x in my_list)

print(list_)
print(generator)

1. Easy to Implement
Generators can be implemented in a clear and concise way as compared to their
iterator class counterpart.
2. Memory Efficient
Generator implementation of such sequences is memory friendly and is preferred
since it only produces one item at a time.
3. Represent Infinite Stream
Infinite streams cannot be stored in memory, and since generators produce only one
item at a time, they can represent an infinite stream of data.

"""





