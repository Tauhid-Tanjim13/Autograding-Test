# An example


# A pointless function
# with a comment spread over two lines
def myFunction():
    ''' Here is a docstring,
        split over two lines.
    '''
    
    #This function doesn't do anything of substance
    print('Hello',
         'there...')
    
    print('Goodbye' \
          'then...')


myFunction.__doc__
myFunction.__name__
import inspect
inspect.isfunction(myFunction)
inspect.getdoc(myFunction)
inspect.getcomments(myFunction)
inspect.getsource(myFunction)

a=0
b=2

def myfunc(a):
    c=5
    return a+c

hello = myfunc(b)