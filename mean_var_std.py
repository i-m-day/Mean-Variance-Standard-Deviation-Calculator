import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')

    x = np.array(list).reshape(3,3)

    calculations = {}

    func = lambda func, x, ax = None: func(x, axis = ax).tolist()
    methods = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
    }

    for method in methods:
        calculations[method] = [func(methods[method], x, ax) for ax in [0, 1, None]]
        
    return calculations