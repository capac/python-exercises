#! /usr/bin/env python

import math
# import numpy as np
# import matplotlib.pyplot as plt


def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 + math.erf((x - mu) / (math.sqrt(2) * sigma))) / 2


# def normal_cdf_plots(xs, mu, sigma, color):
#     axes.plot(xs, [normal_cdf(x, mu, sigma) for x in xs], color=color,
#               label=f'mu = {mu}, sigma = {sigma}')
#     axes.set_title('Various normal CDFs')
#     axes.legend(loc=4)
#     fig.tight_layout()
#     plt.grid(True, linestyle='--')


# # parameter values
# mu_list = [0, 0, 0, -1]
# sigma_list = [1, 2, 0.5, 1]
# colors = ['dodgerblue', 'forestgreen', 'firebrick', 'darkorchid']

# # plots
# xs = np.linspace(-6, 6, 100)
# fig, axes = plt.subplots(1, 1, figsize=(8, 6))
# for mu, sg, cl in zip(mu_list, sigma_list, colors):
#     normal_cdf_plots(xs, mu, sg, cl)
# plt.show()


def inverse_normal_cdf(p: float, mu: float = 0, sigma: float = 1, tol: float = 1e-5) -> float:
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tol=tol)
    low_z = -10.0
    hi_z = 10.0
    while hi_z - low_z > tol:
        mid_z = (hi_z + low_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z = mid_z
        else:
            hi_z = mid_z
    return mid_z


if __name__ == "__main__":
    p = float(input('Enter a value for p: '))
    # mu = float(input('Enter a value for mu: '))
    # sigma = float(input('Enter a value for sigma: '))
    print(f'The inverse is: {inverse_normal_cdf(p, mu=0, sigma=1)}')
