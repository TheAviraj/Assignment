import numpy as np
import matplotlib.pyplot as plt
 

barWidth = 0.2
fig = plt.subplots(figsize =(12,12))
 
a = [10,20,30,40,50,60,70,80,90,100,110]
b = [5,10,15,20,25,30,35,40,45,50,55]
c = [8,16,24,32,40,48,56,64,72,80,88]
d = [9,18,27,36,45,54,63,72,81,90,99]

br1 = np.arange(len(a))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]

plt.bar(br1, a, color ='r', width = barWidth,
        edgecolor ='grey', label ='a')
plt.bar(br2, b, color ='g', width = barWidth,
        edgecolor ='grey', label ='b')
plt.bar(br3, c, color ='b', width = barWidth,
        edgecolor ='grey', label ='c')
plt.bar(br4, d, width = barWidth,
        edgecolor ='grey', label ='d')
 

plt.xlabel('x-axis', fontweight ='bold', fontsize = 15)
plt.ylabel('y-axis', fontweight ='bold', fontsize = 15)
plt.legend()
plt.show()
