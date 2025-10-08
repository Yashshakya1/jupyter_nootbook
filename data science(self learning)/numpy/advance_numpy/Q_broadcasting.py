# Convert Celsius to Fahrenheit for many values
import numpy as np
temp_celsius = np.array([0,20,40,70,100])
Fahrenheit = temp_celsius * 9/5 + 32
print(Fahrenheit)
print(type(Fahrenheit))