import warnings
warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy import log
from pandas import Series
from pandas import datetime

# =============================================================================
# def parser(x):
# 	return datetime.strptime(''+x, '%d/%m/%Y')
# =============================================================================

Temperature = pd.read_csv('C:\\Users\\faaiz\\Documents\\2 semester\\DDA\\EXC\\QADRI_ex5\\daily-minimum-temperatures-in-me.csv', header=0,
	index_col=0, squeeze=True, parse_dates=True)
AirPassengers = pd.read_csv('C:\\Users\\faaiz\\Documents\\2 semester\\DDA\\EXC\\QADRI_ex5\\air-passengers\\AirPassengers.csv', header=0,
	parse_dates=[0], index_col=0, squeeze=True)

def stationary_check(data):
    data.hist()
    plt.show()
    
    X = data.values
    X = X.astype('float32')
    split = int(len(X) / 2)
    X1, X2 = X[0:split], X[split:]
    mean1, mean2 = X1.mean(), X2.mean()
    var1, var2 = X1.var(), X2.var()
    std1, std2 = X1.std(), X2.std()
    print('mean1=%f, mean2=%f' % (mean1, mean2))
    print('variance1=%f, variance2=%f' % (var1, var2))
    print('std1=%f, std2=%f' % (std1, std2))
    # Tail-rolling average transform
    rolling = data.rolling(window=3)
    rolling_mean = rolling.mean()
    rolling_std = rolling.std()
    # plot original and transformed dataset
    plt.plot(data, color='blue', label = 'original data')
    plt.plot(rolling_mean, color='red', label = 'data after mean')
    plt.plot(rolling_std, color='green', label = 'standard deviation')
    plt.legend(loc='upper left')
    plt.show()

def  smoothing_technique(data):
    X = data.values
    X = log(X)
    split = int(len(X) / 2)
    X1, X2 = X[0:split], X[split:]
    mean1, mean2 = X1.mean(), X2.mean()
    var1, var2 = X1.var(), X2.var()
    std1, std2 = X1.std(), X2.std()
    print('mean1=%f, mean2=%f' % (mean1, mean2))
    print('variance1=%f, variance2=%f' % (var1, var2))
    print('std1=%f, std2=%f' % (std1, std2))
    plt.hist(X)
    plt.show()
    plt.plot(X)
    plt.show()

stationary_check(AirPassengers)
stationary_check(Temperature)
smoothing_technique(AirPassengers)


