import numpy as np
import random



def initialise_splines(N, G):

    #make first segment's coefficients corresponding to t0->t1
    first = np.random.normal(0, 1, size=(N+1))
    free_coefficients = [first]
    all_coefficients = [first]
    #consider the next row
    #firstly let's get the free coefficients in:
    #3 are dependent, so do N-2

    knots = np.linspace(0, 1, G)

    #this block is responsible for adding one knot
    for i in range(1, G):
        Next = np.random.normal(0, 1, size=(N+1))
        all_coefficients.append(Next)
        Next_free = []
        for j in range(0, N-2):
            Next_free.append(Next[j])
        free_coefficients.append(Next_free)

    return(free_coefficients, knots)

        #we need to add G-1 knotslen(free_coefficients)-1

def next_dependents(a, free_b, t):
    #want to calculate b2 b1 b0 for the next row
    N = len(a)
    b = [] #just using range as a placeholder because of sticky array problem
    for i in range(0, 3):
        b.append(0) #placeholder for b2 b1 b0

    for i in range(0, len(free_b)):
        b.append(free_b[i])
    #y the first 3 terms need to be modified
    #print(b)

    b2 = a[2]
    for j in range(3, N):
        b2 += 0.5 * j*(j-1)*(a[j]-b[j])*t**(j-2)
    b[2] = b2

    b1 = a[1]
    for j in range(2, N):
        b1 += j * (a[j] - b[j]) * t ** (j-1)
    b[1] = b1

    b0 = a[0]
    for j in range(1, N):
        b0 += (a[j] - b[j]) * t**j
    b[0] = b0

    #print(b)

    return(b)

def fill_coefficients(free_coefficients, knots):
    all_coefficients = [free_coefficients[0]]
    #next layer
    for i in range(0, len(knots)-1):
        next_layer = next_dependents(all_coefficients[i], free_coefficients[i+1], knots[i+1])
        #print(next_layer)
        all_coefficients.append(next_layer)

    return(all_coefficients)

def B(x, C):
    #C is the row of coefficients for this basis
    #now we can compute the output of our polynomial
    #need to separate into basis functions
    y = 0
    for i in range(0, len(C)):
        y += C[i] * x ** i
    return(y)

#now we want to define the spline function, given the coefficients
def spline(x, coefficients, knots):
    #this ingests all coefficients and outputs blindly; doesn't care which one was free and which one wasn't
    #we require 0<x<1
    #firstly we must determine which interval x is in
    #spline selector
    k = 0

    while (k+1 < len(knots)):
        if x >= knots[k+1]:
            k = k + 1
        else:
            break
    #print(k)
    #now we retrieve the right set of coefficients
    this_set = coefficients[k]

    #compute B usiyng this set of coefficients
    y = B(x, this_set)
    return(y)





