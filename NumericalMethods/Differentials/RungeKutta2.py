### Runge-Kutta method of second order ###

def y_l(x, y):
    return x*x + y*y

def runga_kutta(x, y, a, b, h):
    while (x < b-0.01): 
        x_previous = x
        x = x_previous + h
        y = y + h*y_l(x_previous + h/2, y + h/2*y_l(x_previous, y))

    print(x, y)
    return y

runga_kutta(0, 0, 0, 1.4, 1)

r1 = runga_kutta(0, 0, 0, 1.4, 0.1)
r2 = runga_kutta(0, 0, 0, 1.4, 0.1/2)
r3 = runga_kutta(0, 0, 0, 1.4, 0.1/4)

quotient = (r2 - r1)/(r3 - r2)
print("quotient = ", quotient)
err = (r3-r2)/3
print("error", err)