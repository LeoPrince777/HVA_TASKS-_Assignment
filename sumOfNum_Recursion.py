def sum_num(n):
    if n<=0:
        return n
    return n+sum_num(n-1)
print(sum_num(7))

def sum_num(a):
    if not a:
        return 0
    else:
        return a[0]+sum_num(a[1:])
    
a=[3,5,2,4]    
print(sum_num(a))

def greet():
    a= input()
    print(len(a))
greet()

def greet(*n):
    i=0
    for i in n:
        i+=1
greet(5555)
    
    
    
    
