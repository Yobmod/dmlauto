import numpy as np                        # type: ignore
import matplotlib.pyplot as plt            # type: ignore
from scipy.stats import linregress        # type: ignore
from typing import List, Tuple, Union, NoReturn, Optional, Any

# types
TupFlType = Tuple[float, ...]
OptTupFlType = Optional[TupFlType]
NumType = Union[int, float]
IterNumType = Union[List[NumType], Tuple[NumType, ...]]

# constants

# data
vol_water = [1, 2, 3, 4, ]


# calcs
def calc_BET_y(vol_water: IterNumType) -> Tuple[float, ...]:
    part_press = (1.2, 2.2, )
    BET_y = part_press
    return BET_y        # P/P0 (water)


def calc_BET_x(vol_water: IterNumType, V: IterNumType) -> Tuple[float, ...]:
    return BET_x                    # P/V(P0-P)


BET_x = (0.1, 0.2, 0.3, 0.4)     # P/P0 (water)
BET_y = (40, 80, 100, 130)          # P/V(P0-P)
err_x = (0.01, 0.04, 0.02, 0.05)
err_y = (0.2, 0.3, 0.5, 0.9)

min_x = np.subtract(BET_x, err_x)
min_y = np.subtract(BET_y, err_y)
max_x = np.add(BET_x, err_x)
max_y = np.add(BET_y, err_y)


def plot_BET(BET_x: TupFlType, BET_y: TupFlType,
             err_x: OptTupFlType=None, err_y: OptTupFlType=None) -> NoReturn:
    linfit = np.polyfit(BET_x, BET_y, 1)     # linear regression, var = [gradient, intercept]
    linfit_func = np.poly1d(linfit)                    # trendline
    plt.plot(BET_x, linfit_func(BET_x), 'g')

    plt.scatter(BET_x, BET_y, s=20, c='g')
    plt.axis([0, 0.5, 0, 200])        # [xmin, xmax, ymin, ymax]
    plt.show()

    lininfo = linregress(BET_x, BET_y)
    print(lininfo)           # var = (gradient, intercept, r-val, p-val, sterr(grad), )
    BET_line_eqn = "y=%.6fx+(%.6f)" % (linfit[0], linfit[1])
    print(BET_line_eqn)


plot_BET(BET_x, BET_y)

minmin = linregress(min_x, min_y)
minmax = linregress(min_x, max_y)
maxmax = linregress(max_x, max_y)
maxmin = linregress(max_x, min_y)

print(minmin)
print(minmax)
print(maxmin)
print(maxmax)

ave_stderr = (minmin[4] + minmax[4] + maxmin[4] + maxmax[4]) / 4
ave_slope = (minmin[0] + minmax[0] + maxmin[0] + maxmax[0]) / 4

print(ave_slope)
print(ave_stderr)

#
x_data = []           
for i in range(4):
    d_d = [] 
    d_d.append(BET_x[i])
    d_d.append(min_x[i])
    d_d.append(max_x[i])
    x_data.append(d_d)  # x_data = list ofx1, x2, x3....

y_data = []           
for i in range(4):
    d_d = [] 
    d_d.append(BET_y[i])
    d_d.append(min_y[i])
    d_d.append(max_y[i])
    y_data.append(d_d)  # x_data = list ofx1, x2, x3....


x_comb = [(a,b,c,d) for a in x_data[0] for b in x_data[1] for c in x_data[2] for d in x_data[3]]
y_comb = [(a,b,c,d) for a in y_data[0] for b in y_data[1] for c in y_data[2] for d in y_data[3]]

grads = []
ave_grad = 0
for x in x_comb:
    for y in y_comb:
        plt.plot(x, y, 'g')
        lininfo = linregress(x, y)
        grads.append(lininfo[0])
        ave_grad += lininfo[0]
plt.show()
print(ave_grad / len(x_comb))