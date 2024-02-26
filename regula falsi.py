import matplotlib.pyplot as plt

def func(x):
    return (x*x*x*x - 11*x +8)

def regulafalsi(x0,x1,tol,no):
    i =1
    iteration_numbers = []  
    root_values = []       
    while(i <= no):
        x2 = x1 - (func(x1)*(x1-x0))/(func(x1)-func(x0))
        iteration_numbers.append(i)   
        root_values.append(x2)   
        if(abs(x2-x1)<tol or abs(x2-x0)<tol):
            print("The value of root is: %.5f" % x2)
            break
        else:
            i = i+1
            if(func(x2)*func(x1)<0):
                x0 = x2
            else:
                x1 = x2
    
    else:
        print("Method failed to converge within the specified number of iterations = %.0f" % no)
    
    plt.plot(iteration_numbers, root_values, marker='o')
    plt.xlabel('Iteration Number')
    plt.ylabel('Root Value')
    plt.title('Regula Falsi Method')
    plt.grid(True)
    plt.show()

regulafalsi(1,2,.000001,100)


