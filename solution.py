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

# #Scatter Plot
# plt.scatter(x,y)
# plt.show()

#Calculating Mean Squared Error
def grad_desc(x,y):
    m_curr = b_curr = 0.0
    iterations = 1000000
    n = len(x)
    learning_rate = 0.001
    for i in range(iterations):
        y_pred = m_curr*x + b_curr
        md = -(2/n)*sum(x*(y-y_pred))
        bd = -(2/n)*sum(y-y_pred)
        cost = (1/(2*n))*sum([val**2 for val in (y-y_pred)])
        m_curr = m_curr - learning_rate*md
        b_curr = b_curr - learning_rate*bd
        #print("m:{}, b:{}, cost:{}, iteration{} ".format(m_curr,b_curr,cost,i))
    return [m_curr,b_curr]

x = np.array(x,dtype=float)
y = np.array(y,dtype=float)


theta1, theta0 = grad_desc(x,y)



with open('final-data-test.csv','r') as datafile:
    reader = csv.reader(datafile)
    data = list(reader)

print("Number of data points we have: ",len(data))
x = []
y = []


for i in range(1,len(data)):
    x.append(data[i][0])
    y.append(data[i][1])

x = np.array(x,dtype=float)
y = np.array(y,dtype=float)
sum = 0

for i in range(len(x)):
    sum += math.pow(((theta1*x[i] + theta0) - y[i]),2)

print(sum/1000)