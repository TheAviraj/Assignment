#Question 1
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
a=np.arange(40,50)
b=np.arange(50,60)
plt.plot(a,b)

#Question 2
import matplotlib.pyplot as plt
import numpy as np
days = [1,2,3,4,5,6,7]
sales_1 = [160,150,140,145,175,165,180]
sales_2 = [70,90,160,150,140,145,175]
plt.plot(days,sales_1)
plt.plot(days,sales_2)

#Question 3
import matplotlib.pyplot as plt
import numpy as np
x = [1,2,3,4]
y1 = [4,3,2,1]
y2 = [10,20,30,40]
y3 = [40,30,20,10]
y4 = [1,2,1,2]
y5 = [40,70,90,70]

plt.subplot(3,3,1)
plt.plot(x,y1)
plt.subplot(3,3,2)
plt.plot(x,y2)
plt.subplot(3,3,3)
plt.plot(x,y3)
plt.subplot(3,3,4)
plt.plot(x,y4)
plt.subplot(3,3,5)
plt.plot(x,y5)
