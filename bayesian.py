# provide some functions for learning bayesian statistics
from math import *

def choose(n,k):
    '''calculate binomial coefficent
        (n k) = n! / (k!*(n-k)!)
    '''
    return int(factorial(n)/(factorial(k)*factorial(n-k)))

def binomial(k,n,p):
    '''calculate binomial distribution
        B(k;n,p) = (n k) * p^k * (1-p)^(n-k)
    '''
    return choose(n,k) * p**k * (1-p)**(n-k)

def pbinom(k,n,p,lower_tail=True):
    '''sum up binomial distribution'''

    sum = 0
    if lower_tail:
        for i in range(k+1):
            sum += binomial(i,n,p)
    else:
        for i in range(k+1,n):
            sum += binomial(i,n,p)
    return sum

def beta(p,alpha,beta):
    '''probability density function (PDF)'''
    pass

