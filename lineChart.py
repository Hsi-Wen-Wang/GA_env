import csv
import matplotlib.pyplot as plt

with open('processing.csv',  newline='') as csvfile:
    rows = csv.reader(csvfile)
    listProcess = list(rows)

x = []
y = []

for i in range(len(listProcess)-1):
    x.append(float(listProcess[i+1][0]))
    y.append(float(listProcess[i+1][1]))
plt.figure(figsize=(16,6), dpi=100, linewidth=2)
plt.plot(x, y, color='blue')

# plt.xlim(0,10)
plt.ylim(0,100)

plt.xlabel('iter times', fontsize = '10')
plt.ylabel('total time', fontsize = '10')

plt.show()
