# Team Details:
# Member 1 Name: Vaibhav Khamesra
# Member 2 Name: Ronit Gupta
# Member 1 Roll Number: 21UCS224
# Member 2 Roll Number: 21UCS173

import csv
import matplotlib.pyplot as plt
import numpy as np
import math

#Extracting the Data from a CSV file
with open('final-data-train.csv','r') as datafile:
    reader = csv.reader(datafile)
    data = list(reader)

print("Number of data points we have: ",len(data))
x = []
y = []


for i in range(1,len(data)):
    x.append(data[i][0])
    y.append(data[i][1])

#Scatter Plot
# plt.scatter(x,y)
# plt.show()

#Calculating Mean Squared Error


x = np.array(x,dtype=float)
y = np.array(y,dtype=float)

data_size = len(x)
sigma_y = 0
sigma_x = 0
sigma_xy = 0
sigma_x2 = 0

for i in range(data_size):
    sigma_y += y[i]
    sigma_x += x[i]
    sigma_xy += x[i]*y[i]
    sigma_x2 += x[i]*x[i]

w0 = (sigma_y*sigma_x2 - sigma_x*sigma_xy)/(data_size*sigma_x2 - sigma_x*sigma_x)
w1 = (data_size*sigma_xy - sigma_x*sigma_y)/(data_size*sigma_x2 - sigma_x*sigma_x)

print(w0,"  ",w1)

sum_squared_regression = 0
expectation_y = sigma_y/data_size
y_pred = []

for i in range(len(x)):
    y_pred.append(w1*x[i] + w0)
    sum_squared_regression += math.pow(((w1*x[i] + w0) - expectation_y),2)

y_pred =np.array(y_pred,dtype=float)
print(sum_squared_regression)


sum_squared_error = 0
for i in range(data_size):
    sum_squared_error += math.pow(y[i] - y_pred[i],2)

print(sum_squared_error)

sum_squared_total = 0
for i in range(data_size):
    sum_squared_total += math.pow(y[i] - expectation_y,2)

print(sum_squared_total)

