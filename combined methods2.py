import matplotlib.pyplot as plt

def func(x):
    return (x*x*x*x - 11*x + 8)

def g1(x):
    return (11*x - 8)**0.25

def df(x):
     return (4*x*x*x - 11)

def bisection(a, b, tol, no):
    fa = func(a)
    iteration_numbers = []  
    root_values = []       
    
    i = 1
    while i <= no:
        p = a + (b - a) / 2
        fp = func(p)
        iteration_numbers.append(i)   
        root_values.append(p)        

        if fp == 0 or (b - a) / 2 < tol:
            print("Bisection: The value of root is: %.5f" % p)
            break
        else:
            i = i + 1
            if fa * fp > 0:
                a = p
                fa = fp
            else:
                b = p
    else:
        print("Bisection: Method failed to converge within the specified number of iterations = %.0f" % no)
    
    plt.subplot(2, 3, 1)
    plt.plot(iteration_numbers, root_values, marker='o')
    plt.xlabel('Iteration Number')
    plt.ylabel('Root Value')
    plt.title('Bisection')


def fixedpoint(x0, tol, no):
    i = 1
    iteration_numbers = []  
    root_values = []       
    while i <= no:
        x1 = g1(x0)
        iteration_numbers.append(i)   
        root_values.append(x1)   
        if abs(x1 - x0) < tol:
            print("Fixed Point: The value of root is: %.5f" % x1)
            break
        else:
            x0 = x1
            i = i + 1
    else:
        print("Fixed Point: Method failed to converge within the specified number of iterations = %.0f" % no)
    
    plt.subplot(2, 3, 2)
    plt.plot(iteration_numbers, root_values, marker='o')
    plt.xlabel('Iteration Number')
    plt.ylabel('Root Value')
    plt.title('Fixed Point')


def newtonsmethod(x0, tol, no):
    i = 1
    iteration_numbers = []  
    root_values = []       
    while i <= no:
        x1 = x0 - func(x0) / df(x0)
        iteration_numbers.append(i)   
        root_values.append(x1)   
        if abs(x1 - x0) < tol:
            print("Newton's Method: The value of root is: %.5f" % x1)
            break
        else:
            x0 = x1
            i = i + 1
    else:
        print("Newton's Method: Method failed to converge within the specified number of iterations = %.0f" % no)
    
    plt.subplot(2, 3, 3)
    plt.plot(iteration_numbers, root_values, marker='o')
    plt.xlabel('Iteration Number')
    plt.ylabel('Root Value')
    plt.title("Newton's Method")


def secantmethod(x0, x1, tol, no):
    i = 1
    iteration_numbers = []  
    root_values = []       
    while i <= no:
        x2 = x1 - (func(x1) * (x1 - x0)) / (func(x1) - func(x0))
        iteration_numbers.append(i)   
        root_values.append(x2)   
        if abs(x2 - x1) < tol:
            print("Secant Method: The value of root is: %.5f" % x2)
            break
        else:
            x0 = x1
            x1 = x2
            i = i + 1
    else:
        print("Secant Method: Method failed to converge within the specified number of iterations = %.0f" % no)
    
    plt.subplot(2, 3, 4)
    plt.plot(iteration_numbers, root_values, marker='o')
    plt.xlabel('Iteration Number')
    plt.ylabel('Root Value')
    plt.title('Secant Method')


def regulafalsi(x0, x1, tol, no):
    i = 1
    iteration_numbers = []  
    root_values = []       
    while i <= no:
        x2 = x1 - (func(x1) * (x1 - x0)) / (func(x1) - func(x0))
        iteration_numbers.append(i)   
        root_values.append(x2)   
        if abs(x2 - x1) < tol or abs(x2 - x0) < tol:
            print("Regula Falsi: The value of root is: %.5f" % x2)
            break
        else:
            i = i + 1
            if func(x2) * func(x1) < 0:
                x0 = x2
            else:
                x1 = x2
    
    else:
        print("Regula Falsi: Method failed to converge within the specified number of iterations = %.0f" % no)
    
    plt.subplot(2, 3, 5)
    plt.plot(iteration_numbers, root_values, marker='o')
    plt.xlabel('Iteration Number')
    plt.ylabel('Root Value')
    plt.title('Regula Falsi')



a = 1
b = 2
tol = 0.000001
no = 100

plt.figure(figsize=(10, 6))

bisection(a, b, tol, no)
fixedpoint(b, tol, no)
newtonsmethod(b, tol, no)
secantmethod(a, b, tol, no)
regulafalsi(a, b, tol, no)

plt.tight_layout()
plt.show()
