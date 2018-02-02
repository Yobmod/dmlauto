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


BET_y = (38.05, 63.64, 111.1, 173.0)     # P/P0 (water)
BET_x = (0.0416, 0.1041, 0.2082, 0.3122)          # P/V(P0-P)
err_y = (0.01, 0.04, 0.02, 0.05)
err_x = (0.002, 0.003, 0.005, 0.009)

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

#BET_x = np.array(BET_x)
#slope, intercept, r, prob2, see = linregress(BET_x, BET_y)
#mx = BET_x.mean()
#sx2 = ((BET_x-mx)**2).sum()
#chi2 = see / (sqrt(1.0 / sx2))
#interc_err = chi2  * sqrt((1./len(BET_x)) + mx*mx/sx2)
#print(see, interc_err)


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
#print(y_comb)
  
grads = []; sum_grads = 0
intercepts = []; sum_intercepts = 0
std_errs = []; sum_std_errs = 0
for x in x_comb:
    for y in y_comb:
        lininfo = linregress(x, y)
        #plt.plot(x, y, 'g')
        grads.append(lininfo[0])
        sum_grads += lininfo[0]
        intercepts.append(lininfo[1])
        sum_intercepts += lininfo[1]
        std_errs.append(lininfo[4])
        sum_std_errs += lininfo[4]

ave_grads = sum_grads / len(grads)
ave_intercepts = sum_intercepts / len(intercepts)
ave_std_errs = sum_std_errs / len(std_errs)
BET_total_ave = "y=%.6fx+(%.6f)" % (ave_grads, ave_intercepts)
print("BET total ave : " + BET_total_ave, ave_std_errs) 
print(len(grads) ** (1/4))