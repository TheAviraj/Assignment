import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
x= np.arange(0,10)
y= x*x

plt.plot(x,y,'ro', linestyle='dashed',linewidth=2, markersize=12)
plt.xlabel('X-axis', color='blue')
plt.ylabel('Y-axis', color='blue')
plt.title('Assignment-1', color='red')
