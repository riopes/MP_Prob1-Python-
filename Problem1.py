import matplotlib.pyplot as plt

x = []                      #Telling python that x and y
y = []                      #are going to become an array or list
n = list(range(100))        #Declaring n as a list of 0 to 99 number with 1 increment

def f(n):                   #Piecewise function that evaluates n as it goes through
    if n <= 9:              #the whole list of n numbers
        f1 = n **(2) - 7    #When n is <= 9, it does the if equation,
    else:                   # when n is greater, it does the recursive function 
        f1 = f(n-10)        #calling n - 10
    return f1

for a in n:                 #Places in x the values of n when a is in n
    x.append(a)             #Also places values in y using the function "f(n)" 
    y.append(f(a))          #defined earlier

plt.stem(x,y,markerfmt='.')
plt.grid()                  #Plots the given x and y using 
plt.show()                  #stem of matplotlib.pyplot