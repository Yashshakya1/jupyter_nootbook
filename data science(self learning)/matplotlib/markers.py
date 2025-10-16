import matplotlib.pyplot as plt 
import numpy as np 
y_points = np.array([8,8,1,5,7,8,7,0,4,4])
plt.plot(y_points, marker = "X")
plt.show()

'''
'o'	  Circle	
'*'	  Star	
'.'	  Point	
','	  Pixel	
'x'	  X	
'X'	  X (filled)	
'+'	  Plus	
'P'	  Plus (filled)	
's'	  Square	
'D'	  Diamond	
'd'	  Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline	

'''

# Format Strings fmt
# This parameter is also called fmt, and is written with this syntax:

# marker|line|color

y_points = np.array([8,8,1,5,7,8,7,0,4,4])
plt.plot(y_points, '*:m')
plt.show()

# Line Reference 
'''
Line Syntax	Description
'-'     Solid line	
':'	    Dotted line	
'--'	Dashed line	
'-.'	Dashed/dotted line
'''

# Color Reference

'''
Color Syntax	Description
'r'	                Red	
'g'	                Green	
'b'	                Blue	
'c'	                Cyan	
'm'	                Magenta	
'y'	                Yellow	
'k'	                Black	
'w'	                White
'''

# Marker Size 
# You can use the keyword argument markersize(ms) or the shorter version,
#  ms to set the size of the markers:

y = np.arange(1,11)
plt.plot(y , marker = 'p' , ms = 20)
plt.show()


# Marker Color
# You can use the keyword argument markeredgecolor(mec) or the shorter 
# mec to set the color of the edge of the markers:
y = np.arange(1,11)
plt.plot(y , marker = 'p' , ms = 20, mec = "y")
plt.show()

# the keyword argument markerfacecolor(mfc) or the shorter mfc 
# to set the color inside the edge of the markers:

y = np.arange(1,11)
plt.plot(y , marker = 'D' , ms = 20, mec = "k", mfc = 'g')
plt.show()

# You can also use Hexadecimal color values: 
y = np.arange(1,11)
plt.plot(y , marker = 'D' , ms = 20, mec = "#367588", mfc = '#B0B0B0')
plt.show()

# Or any of the 140 supported color names.
# LIKE hotpink