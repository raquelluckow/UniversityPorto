### Euler's numerical method ###

def y_l(x,y):
    return x*x + y*y

def Euler(x,y,a,b,h):
    while (x < b-0.001):                  
        x_previous = x
        x = x_previous + h
        y = y + h*y_l(x_previous,y)
    print("x:",x)
    return y


# Calculating the error
h = 0.1

r1 = Euler(0,0,0,1.4,0.1)
r2 = Euler(0,0,0,1.4,0.1/2)
r3 = Euler(0,0,0,1.4,0.1/4)
r4 = Euler(0,0,0,1.4,0.1/8)

print("y1:",r1)
print("y2:",r2)
print("y3:",r3)
quotient = (r3 - r2)/(r4 - r3)           
err = (r4 - r3)
print("quotient", quotient) 
print("err:", err)
