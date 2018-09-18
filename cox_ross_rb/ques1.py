import numpy as np


S0 = 100
sigma = 0.3
r = b = 0.05
T = 2


def coeffs(T, n, b, sigma):
    """
    Coefficients for the n-periods binomial model.
    """
    hn = T/n
    return (
        np.exp(b*hn + sigma*np.sqrt(hn)),
        np.exp(b*hn - sigma*np.sqrt(hn))
    )


def Sn(T, n, b, sigma, j):
    """
    Vector of all possible prices for the option.
    """
    u, d = coeffs(T, n, b, sigma)
    indices = np.arange(0, j)
    return np.power(u, j-indices)*np.power(d, indices)


snj = Sn(T, 3, b, sigma, 5)
print(snj)
