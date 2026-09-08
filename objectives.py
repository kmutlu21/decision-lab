"""Objective families and normalization shared by the importer and API."""
import numpy as np
from scipy.optimize import minimize_scalar

MAXIMUM_METHOD = 'default_model_grid10000_grid200_bounded_v1'


def evaluate(x, family, parameters):
    if family == 'gaussian':
        return sum(parameters[f'a_{i}'] * np.exp(-parameters[f'b_{i}'] * (x - parameters[f'c_{i}']) ** 2) for i in range(1, 4))
    if family == 'cauchy':
        return sum(parameters[f'a_{i}'] / ((x - parameters[f'b_{i}']) ** 2 + parameters[f'c_{i}']) for i in range(1, 4))
    raise ValueError(f'Unknown objective family: {family}')


def estimate_maximum(family, parameters, xmin, xmax):
    # Reproduce save_sequences_delta_default.py's numerical procedure.
    # This is an estimate, not a guarantee of the exact global optimum.
    negative = lambda x: -evaluate(x, family, parameters)
    grid = np.array([evaluate(x, family, parameters) for x in np.linspace(xmin, xmax, 10000)])
    seed_max = max(-negative(x) for x in np.linspace(xmin, xmax, 200))
    result = minimize_scalar(negative, bounds=(xmin, xmax), method='bounded')
    maximum = float(max(grid.max(), seed_max, -result.fun))
    if not np.isfinite(maximum) or maximum <= 0:
        raise ValueError('Normalization requires a finite positive maximum.')
    return maximum
