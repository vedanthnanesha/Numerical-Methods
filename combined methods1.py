import matplotlib.pyplot as plt

def func(x):
    return (x*x*x*x - 11*x + 8)

def g1(x):
    return (11*x -8)**.25

def df(x):
     return (4*x*x*x - 11)

def bisection(a, b, tol, no):
    fa = func(a)
    iteration_numbers = []  
    root_values = [] 
    function_values = []  
    
    i = 1
    while i <= no:
        p = a + (b - a) / 2
        fp = func(p)
        iteration_numbers.append(i)   
        root_values.append(p)      
        function_values.append(fp)  

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
    
    axs[0].plot(iteration_numbers, root_values, marker='o', label='Bisection')
    axs[1].plot(iteration_numbers,function_values,marker='o',label='Bisection')


def fixedpoint(x0, tol, no):
    i = 1
    iteration_numbers = []  
    root_values = []     
    function_values =[]  
    while i <= no:
        x1 = g1(x0)
        iteration_numbers.append(i)   
        root_values.append(x1) 
        function_values.append(func(x1))  
        if abs(x1 - x0) < tol:
            print("Fixed Point: The value of root is: %.5f" % x1)
            break
        else:
            x0 = x1
            i = i + 1
    else:
        print("Fixed Point: Method failed to converge within the specified number of iterations = %.0f" % no)
    
    axs[0].plot(iteration_numbers, root_values, marker='o', label='Fixed Point')
    axs[1].plot(iteration_numbers,function_values,marker='o',label='Fixed Point')


def newtonsmethod(x0, tol, no):
    i = 1
    iteration_numbers = []  
    root_values = []   
    function_values = []    
    while i <= no:
        x1 = x0 - func(x0) / df(x0)
        iteration_numbers.append(i)   
        root_values.append(x1)   
        function_values.append(func(x1))
        if abs(x1 - x0) < tol:
            print("Newton's Method: The value of root is: %.5f" % x1)
            break
        else:
            x0 = x1
            i = i + 1
    else:
        print("Newton's Method: Method failed to converge within the specified number of iterations = %.0f" % no)
    
    axs[0].plot(iteration_numbers, root_values, marker='o', label='Newtons')
    axs[1].plot(iteration_numbers,function_values,marker='o',label='Newtons')


def secantmethod(x0, x1, tol, no):
    i = 1
    iteration_numbers = []  
    root_values = []    
    function_values=[]   
    while i <= no:
        x2 = x1 - (func(x1) * (x1 - x0)) / (func(x1) - func(x0))
        iteration_numbers.append(i)   
        root_values.append(x2)   
        function_values.append(func(x2))
        if abs(x2 - x1) < tol:
            print("Secant Method: The value of root is: %.5f" % x2)
            break
        else:
            x0 = x1
            x1 = x2
            i = i + 1
    else:
        print("Secant Method: Method failed to converge within the specified number of iterations = %.0f" % no)
    
    axs[0].plot(iteration_numbers, root_values, marker='o', label='Secant')
    axs[1].plot(iteration_numbers,function_values,marker='o',label='Secant')


def regulafalsi(x0, x1, tol, no):
    i = 1
    iteration_numbers = []  
    root_values = []     
    function_values = []  
    while i <= no:
        x2 = x1 - (func(x1) * (x1 - x0)) / (func(x1) - func(x0))
        iteration_numbers.append(i)   
        root_values.append(x2)   
        function_values.append(func(x2))
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
    
    axs[0].plot(iteration_numbers, root_values, marker='o', label='Regula Falsi')
    axs[1].plot(iteration_numbers,function_values,marker='o',label='Regula Falsi')



a = 1
b = 2
tol = 0.000001
no = 100

fig, axs = plt.subplots(2, 1, figsize=(10, 8))

bisection(a, b, tol, no)
fixedpoint(b, tol, no)
newtonsmethod(b, tol, no)
secantmethod(a, b, tol, no)
regulafalsi(a, b, tol, no)

axs[0].set_xlabel('Iteration Number')
axs[0].set_ylabel('Root Value')
axs[0].set_title('Root Value Vs Iterations for Different Methods')
axs[0].legend()
axs[0].grid(True)

axs[1].set_xlabel('Iteration Number')
axs[1].set_ylabel('Function Value')
axs[1].set_title('Function Value Vs Iterations for Different Methods')
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()

