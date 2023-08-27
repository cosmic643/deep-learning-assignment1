# Team Details:
# Member 1 Name: Vaibhav Khamesra
# Member 2 Name: Ronit Gupta
# Member 1 Roll Number: 21UCS224
# Member 2 Roll Number: 21UCS173

import csv
import matplotlib.pyplot as plt

with open('final-data-train.csv','r') as datafile:
    reader = csv.reader(datafile)
    data = list(reader)

print("Number of data points we have: ",len(data)-1)
x = []
y = []


for i in range(1,len(data)):
    x.append(data[i][0])
    y.append(data[i][1])

#Scatter Plot
plt.scatter(x,y)
plt.show()
plt.savefig("linear_regression_plot.jpg")