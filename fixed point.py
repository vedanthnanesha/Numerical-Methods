import matplotlib.pyplot as plt

def func(x):
    return (x*x*x*x - 11*x +8)

def g1(x):
    return (11*x -8)**.25

def fixedpoint(x0,tol,no):
    i =1
    iteration_numbers = []  
    root_values = []       
    while(i <= no):
        x1 = g1(x0)
        iteration_numbers.append(i)   
        root_values.append(x1)   
        if(abs(x1-x0)<tol):
            print("The value of root is: %.5f" % x1)
            break
        else:
            x0 = x1
            i = i +1
    else:
        print("Method failed to converge within the specified number of iterations = %.0f" % no)
    
    plt.plot(iteration_numbers, root_values, marker='o')
    plt.xlabel('Iteration Number')
    plt.ylabel('Root Value')
    plt.title('Fixed Point Iterations')
    plt.grid(True)
    plt.show()

fixedpoint(2,.000001,100)


