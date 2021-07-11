#Question 1
'''The Plotly Python graphing library is a scientific graphing library. 
Graphs can be styled with Python and a GUI, and shared with a URL for others to view, collaborate, or save a copy.'''

#Question 2
'''Plotly allows users to import, copy and paste, or stream data to be analyzed and visualized.
For analysis and styling graphs, Plotly offers a Python sandbox (NumPy supported), datagrid, and GUI.
Python scripts can be saved, shared, and collaboratively edited in Plotly.'''

#Question 3

from matplotlib import pyplot as plt
import numpy as np
  
  
cars = ['AUDI', 'BMW', 'FORD',
        'TESLA', 'JAGUAR', 'MERCEDES']
  
data = [23, 17, 35, 29, 12, 41]
  
fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels = cars)
  
plt.show(data)

#Question 4

import numpy as np
import matplotlib.pyplot as plt
 
data = {'Andhra Pradesh':35325, 'Telangana':11964, 'Tamil Nadu':35294,'Karnataka':44869,'Kerala':104508,
        'Madhya Pradesh':479,'Maharashtra':126454,'Puducherry':2006,'Odisha':26922,'Goa':2087}
states = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (20, 10))
 
plt.bar(states, values, color ='maroon',
        width = 0.2)
 
plt.ylabel("states")
plt.xlabel("No. of active cases recorded on July 5")
plt.title("Bar Chart with India's covid-19 Active cases on July 5")
plt.show()

#Question 5

import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

months = ["July","Aug","Sept","Oct","Nov","Dec","Jan","Feb","Mar","Apr","May","June"]
recovery  = [653,1977,3542,5988,7958,9860,10162,10510,11107,12671,19250,28765]

plt.xlabel('months')
plt.ylabel('Recovery (in thousand)')
plt.title("Bar Chart with India's covid-19 Active cases on July 5Line Chat with India's active covid-19 case recovery", fontweight ='bold')
plt.plot(months,recovery)
