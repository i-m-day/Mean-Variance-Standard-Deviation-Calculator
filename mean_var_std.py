import numpy as np

def calculate(list):
    arr = np.array(list).reshape(3, 3)
    mean_Val = [arr.mean(axis = 0).tolist(), arr.mean(axis = 1).tolist(),arr.mean().item()]
    calc_Varience = [arr.var(axis = 0).tolist(), arr.var(axis = 1).tolist(),arr.var().item()]
    calc_Min = [arr.min(axis = 0).tolist(), arr.min(axis = 1).tolist(),arr.min().item()]
    calc_Max = [arr.max(axis = 0).tolist(), arr.max(axis = 1).tolist(),arr.max().item()]
    calc_Std = [arr.std(axis = 0).tolist(), arr.std(axis = 1).tolist(),arr.std().item()]
    calc_Sum = [arr.sum(axis = 0, dtype = 'int32').tolist(), arr.sum(axis = 1, dtype = 'int32').tolist(),arr.sum(dtype = 'int32').item()]
    calculations = {'mean': mean_Val, 'variance': calc_Varience,'standard deviation': calc_Std,
                    'min': calc_Min, 'max': calc_Max, 'sum': calc_Sum}
    return calculations
