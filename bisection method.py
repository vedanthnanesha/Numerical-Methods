import matplotlib.pyplot as plt

def func(x):
    return (x*x*x*x - 11*x + 8)

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
            print("The value of root is: %.5f" % p)
            break
        else:
            i = i + 1
            if fa * fp > 0:
                a = p
                fa = fp
            else:
                b = p
    else:
        print("Method failed to converge within the specified number of iterations = %.0f" % no)
    
    plt.plot(iteration_numbers, root_values, marker='o')
    plt.xlabel('Iteration Number')
    plt.ylabel('Root Value')
    plt.title('Bisection Method Iterations')
    plt.grid(True)
    plt.show()

a = 1
b = 2
tol = 0.000001
no = 100
bisection(a, b, tol, no)

