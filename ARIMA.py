import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from pandas import datetime
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.tsa.arima_model import ARIMA
from pandas import DataFrame
from sklearn.metrics import mean_squared_error


# =============================================================================
# def parser(x):
# 	return datetime.strptime(''+x, '%Y-%m')
# 
# =============================================================================
Temperature = pd.read_csv('C:\\Users\\faaiz\\Documents\\2 semester\\DDA\\EXC\\QADRI_ex5\\daily-minimum-temperatures-in-me.csv', header=0, index_col=0, squeeze=True, parse_dates=True)
AirPassengers = pd.read_csv('C:\\Users\\faaiz\\Documents\\2 semester\\DDA\\EXC\\QADRI_ex5\\air-passengers\\AirPassengers.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)

def ARIMA_model(series):
	X = series.values
	X = X.astype('float32')

	size = int(len(X) * 0.66)
	train, validation = X[0:size], X[size:len(X)]
	history = [x for x in train]
	predictions = list()
	for t in range(len(validation)):
		model = ARIMA(history, order=(5,1,0))
		model_fit = model.fit(disp=0)
		output = model_fit.forecast()
		yhat = output[0]
		predictions.append(yhat)
		obs = validation[t]
		history.append(obs)
		print('predicted=%f, expected=%f' % (yhat, obs))
	error = mean_squared_error(validation, predictions)
	print('Test MSE: %.3f' % error)
	# plot
	plt.plot(validation, label = 'validation')
	plt.plot(predictions, color='red', label = 'predictions')
	plt.legend(loc='upper left')
	plt.show()

ARIMA_model(AirPassengers)
#ARIMA_model(Temperature)