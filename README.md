# KAN-single-layer
Single Layer KAN network with one input node, one output node and 1 activation function connecting them. Made from scratch in Python. 

Uses basic commands and numpy for faster arrays. See KAN.py for a more explicit code layout; the optimised version uses multiprocessing and more "implicit" variables to run faster but may be less intuitive toread. No other libraries were used, no Pytorch, flax etc...

Run main.py. It trains the model according to some input data then plots a graph of what it has learnt about your input data within the interval [0, 1]
We expect all input data to be within the range of [0, 1].

Defaults:
training data: samples from a sin curve with a bit of Gaussian noise added. 
activation function:
A(x) = Phi(x) = (silu(x) + spline(x)) * w
spline(x) is made of 10 basis splines (B-splines) situated between 10 knot points, corresponding to a total grid size of 10. Each B-spline is a polynomial up to x**3

![single layer single spline KAN](https://github.com/robinli87/KAN-single-layer/assets/101805462/01cbe136-3eef-439b-80cf-396accf82d95)
