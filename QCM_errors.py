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

total_error = np.multiply(err_x, err_y)
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
    print("BET line : " + BET_line_eqn)

plot_BET(BET_x, BET_y)

minmin = linregress(min_x, min_y)
minmax = linregress(min_x, max_y)
maxmax = linregress(max_x, max_y)
maxmin = linregress(max_x, min_y)

# print(minmin)
# print(minmax)
# print(maxmin)
# print(maxmax)

ave_stderr = (minmin[4] + minmax[4] + maxmin[4] + maxmax[4]) / 4
ave_slope = (minmin[0] + minmax[0] + maxmin[0] + maxmax[0]) / 4
ave_interc = (minmin[1] + minmax[1] + maxmin[1] + maxmax[1]) / 4

BET_ave_eqn = "y=%.6fx+(%.6f)" % (ave_slope, ave_interc)
print("BET ave : " + BET_ave_eqn)

m, c = np.polyfit(BET_x, BET_y, 1, w = [1.0 / ty for ty in total_error])

BET_weighted = "y=%.6fx+(%.6f)" % (m, c)
print("BET weight : " + BET_weighted)

from math import sqrt

BET_x = np.array(BET_x)
slope, intercept, r, prob2, see = linregress(BET_x, BET_y)
mx = BET_x.mean()
sx2 = ((BET_x-mx)**2).sum()
sd_intercept = see * sqrt((1./len(BET_x)) + mx*mx/sx2)
sd_slope = see * sqrt(1./sx2)

print(sd_slope, sd_intercept)