import matplotlib.pyplot as plt
plt.style.use('seaborn')
from numpy import array
import pandas as pd
import numpy as np

df = pd.Series.from_csv('child_rape.csv', header = 0)
plt.plot(df, color='black', alpha = 0.8)

df = pd.read_csv('child_rape.csv')
x = df['month']
y = df['rape_count']

ax = plt.axes()

plt.bar(x, y, width=.85, facecolor='red', alpha = 0.5)
ylabel = np.arange(0, 150, 10)
xLabel = []
for i in range(len(x) - 1):
    if (i == 0) or (i % 3 == 0):
        xLabel.append(x[i])
    else:
        xLabel.append('')
xLabel = array(xLabel)

plt.xticks(xLabel, xLabel)
plt.yticks(ylabel, ylabel)
plt.title('Child rape scenario in Bangladesh in recent years')
#plt.xlabel('Months', fontsize = 13)
plt.ylabel('# of child got raped per month', fontsize = 13)

a = -0.26
for j, i in enumerate(y):
    if(i < 10):
        ax.text(a + .135, 2, str(i), color='white')
    elif(i > 99):
        ax.text(a - .135, 2, str(i), color='white')        
    else:
        ax.text(a + 0.02 , 2, str(i), color='white')
    a = a + 1

plt.show()
