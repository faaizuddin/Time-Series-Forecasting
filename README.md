# Time-Series-Forecasting
This repository is about Time Series Forecasting in Python. It also includes checking whether the data is stationary or not. The two datasets used are "daily temperature" and "air passengers".

The first part of this repository is to check the stationarity of the dataset and to make it stationary if not.

A stationary process has the property that the mean, variance and autocorrelation structure do not change over time.
To find data stationarity, we will find out summary statistics, have a look at plot lines and histograms.

It can be seen, for the Air Passengers dataset, the difference in mean between the two splits is large, as well as the variance and the standard deviation. 
![alt text](https://github.com/faaizuddin/Time-Series-Forecasting/blob/master/HistAP.png)
![alt text](https://github.com/faaizuddin/Time-Series-Forecasting/blob/master/AP.png)
Through the histogram and the plotlines, we can see that there is an obvious seasonality component, and it looks like the seasonality component is growing. This may suggest an exponential growth from season to season.

Now for the Daily Temperature dataset:
![alt text](https://github.com/faaizuddin/Time-Series-Forecasting/blob/master/HistTemp.png)
![alt text](https://github.com/faaizuddin/Time-Series-Forecasting/blob/master/Temp.png)

The graphs clearly show that the time series is not following any trend or seasonality. Therefore, it is stationary. It can be seen through the mean values.

Now I will apply smoothing technique, i.e. rolling averages to make time series stationary. Smoothing is a technique applied to time series to remove the fine-grained variation between time steps. The hope of smoothing is to remove noise and better expose the signal of the underlying causal processes. Moving averages are a simple and common type of smoothing used in time series analysis and time series forecasting.
But to make a time series stationary, two other common ways are used, differencing and transform (log transform). I applied log transform on Passenger dataset to make it stationary.
By using log transform, all of the statistical values are almost the same, which suggests that that has moved on towards stationarity.
![alt text](https://github.com/faaizuddin/Time-Series-Forecasting/blob/master/APLog.png)
![alt text](https://github.com/faaizuddin/Time-Series-Forecasting/blob/master/APLog1.png)
Through the graphs, the exponential growth seems diminished, but we still have a trend and seasonal elements.

The second part consists of forecasting values through ARIMA model.

I will be using ‘statsmodels.tsa.arima_model’ to import ARIMA.
![alt text](https://github.com/faaizuddin/Time-Series-Forecasting/blob/master/APGraph.png)
Validation dataset is used to check the validation accuracy. The above graph represents the validation values and the predicted values for the ‘Air Passengers’ dataset.
![alt text](https://github.com/faaizuddin/Time-Series-Forecasting/blob/master/TempGraph.png)
The above graph represents the validation values and the predicted values for the ‘Daily Temperature’ dataset.

