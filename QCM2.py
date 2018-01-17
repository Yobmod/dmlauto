import numpy as np

def wlinear_fit (x,y,w) :
    """
    Fit (x,y,w) to a linear function, using exact formulae for weighted linear
    regression. This code was translated from the GNU Scientific Library (GSL),
    it is an exact copy of the function gsl_fit_wlinear.
    """
    # compute the weighted means and weighted deviations from the means
    # wm denotes a "weighted mean", wm(f) = (sum_i w_i f_i) / (sum_i w_i)
    W = np.sum(w)
    wm_x = np.average(x,weights=w)
    wm_y = np.average(y,weights=w)
    dx = x-wm_x
    dy = y-wm_y
    wm_dx2 = np.average(dx**2,weights=w)
    wm_dxdy = np.average(dx*dy,weights=w)
    # In terms of y = a + b x
    b = wm_dxdy / wm_dx2
    a = wm_y - wm_x*b
    cov_00 = (1.0/W) * (1.0 + wm_x**2/wm_dx2)
    cov_11 = 1.0 / (W*wm_dx2)
    cov_01 = -wm_x / (W*wm_dx2)
    # Compute chi^2 = \sum w_i (y_i - (a + b * x_i))^2
    term = np.multiply((a+b), x)
    chi2 = np.sum (w * (y-(term))**2)
    return a,b,cov_00,cov_11,cov_01,chi2

BET_x = (0.1, 0.2, 0.3, 0.4)     # P/P0 (water)
BET_y = (40, 80, 100, 130)          # P/V(P0-P)
err_x = (0.01, 0.04, 0.02, 0.05)
err_y = (2.0, 3.0, 5.0, 9.0)

total_error = np.multiply(err_x, err_y)


intercept, slope, cov_00, cov_11, cov_01, chi2 = wlinear_fit(BET_x,BET_y,1.0/total_error**2)

interc_err = cov_00 ** 0.5
slope_err = (cov_11 ** 0.5)

print(slope, intercept, slope_err, interc_err)

import statsmodels.api as sm

mod_wls = sm.WLS(BET_y, BET_x, weights=1./total_error)
res_wls = mod_wls.fit()
print(res_wls.summary2())
# print(dir(res_wls))


