import re
def validate_email(email):
    pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern,email):
        return True
    else:
        return False
    
email1="babirye.mable442@gmail.com"
email2="babiryemable442@gmailcom"
    
print(validate_email(email1))
print(validate_email(email2))
    
    # generators and Iterators
    #yeild
def factorial(n):
        if n==0:
            yield 1
        else:
            return n*factorial(n-1)
           
for i in range(1,10):
        print(factorial(i))

# Example3 
# Generate function that yields the square of numbers from 1 to 10
def squares():
    for i in range(1,10):
        yield i**2
        
# Create an iterator object that yields the square of numbers from 1-10
squares_iterator = squares()

# Print the first 5 square of numbers from 1 to 10
for i in range(5):
    print(next(squares_iterator))
    
# Decorators
def my_decorator(func):
    def inner():
        print("I am inner function")
        func()
    return inner
    
@my_decorator
def outer_decorator():
    print("I am outer function")
    
outer_decorator()    


import threading as mth
def print_cube(num):
    print("Cube:{}".format(num*num*num))
def print_square(num):
    print("Square:{}".format(num*num))
def print_num(num):
    print(num)
    
if __name__=="__main__":
    p1 =mth.Thread(target=print_square,args=(8, ))      
    p2 =mth.Thread(target=print_cube,args=(6, ))
    p3 =mth.Thread(target=print_num,args=(6, ))
    
    p1.start()
    p2.start()
    p3.start()
# Wait unti process 1 is finished
    p1.join()
    p2.join() 
    p3.join()
         
    print("Done")
        
    