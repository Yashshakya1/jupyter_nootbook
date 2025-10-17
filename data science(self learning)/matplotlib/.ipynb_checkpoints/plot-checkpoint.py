# creating a line graphs using the plot method  
import matplotlib.pyplot as plt 
import numpy as np 
# (1,5)   , (2,5)
# (x1,y1) , (x2,y2)
# plot(x-axis , y-axis)

x_axis = np.array([1,10])
y_axis = np.array([1,100])
plt.plot(x_axis,y_axis)
plt.show()

# ploting without the ploting line ' o ' this means 'rings'
x = np.array([1,10])
y = np.array([1,100])
plt.plot(x,y,'o')
plt.show()


# Multiple Points
x1 = np.array([1,3,5,7,8])
y1 = np.array([2,5,6,8,0])
plt.plot(x1,y1,'o')
plt.show()

# Default X-Points
# If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 etc.,
#  depending on the length of the y-points.
y1 = np.array([3, 8, 1, 10, 5, 7])
plt.plot(y1,'o')
plt.show()