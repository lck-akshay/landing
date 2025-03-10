#!/usr/bin/python
import numpy as np
import numpy.linalg as la
import math
import sys

import numpy as np
from scipy import linalg
from scipy.optimize import leastsq

'''
# Generate some data that lies along a line
x = np.array[1,2,3]
y = np.array[1,2,3]
z = np.array[1,2,3]

#x = np.mgrid[-2:5:120j]
#y = np.mgrid[1:9:120j]
#z = np.mgrid[-5:3:120j]

data = np.concatenate((x[:, np.newaxis], 
                       y[:, np.newaxis], 
                       z[:, np.newaxis]), 
                      axis=1)

# Calculate the mean of the points, i.e. the 'center' of the cloud
datamean = data.mean(axis=0)

# Do an SVD on the mean-centered data.
uu, dd, vv = np.linalg.svd(data - datamean)

# Now vv[0] contains the first principal component, i.e. the direction
# vector of the 'best fit' line in the least squares sense.

# Now generate some points along this best fit line, for plotting.

# I use -7, 7 since the spread of the data is roughly 14
# and we want it to have mean 0 (like the points we did
# the svd on). Also, it's a straight line, so we only need 2 points.
linepts = vv[0] * np.mgrid[-7:7:2j][:, np.newaxis]

# shift by the mean to get the line in the right place
linepts += datamean

# Verify that everything looks right.

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as m3d

ax = m3d.Axes3D(plt.figure())
ax.scatter3D(*data.T)
ax.plot3D(*linepts.T)
plt.show()

'''
resource_dir = "../resources/"
data = resource_dir+"dataset4.mat"

file = open(data,"rb")
matrix = [[0 for x in range(500)] for x in range(500)] 

#competiton variables
pixel_resolution = 0.2
lander_diameter = 3.4
lander_footpad = 0.5
lander_belly = 0.39

map_size = 500

linenum = 0;
for line in file:
    data = line.split(" ")
    for i in range(len(data)):
        matrix[linenum][i] =  float(data[i])
    linenum=linenum+1


import numpy as np

x = []
y = []
z = []

for i in range(500):
    for j in range(500):
        x.append(i)
        y.append(j)
        z.append(matrix[i][j])


#XYZ = np.array(matrix)
XYZ = np.array([x,y,z])

XYZ2 = np.array([
[0.274791784, -1.001679346, -1.851320839, 0.365840754],
        [-1.155674199, -1.215133985, 0.053119249, 1.162878076],
        [1.216239624, 0.764265677, 0.956099579, 1.198231236]])

# Inital guess of the plane
p0 = [1.0, 1.0, 1.0, 1.0]

print(len(XYZ))
print(len(XYZ[0]))

print(len(XYZ2))
print(len(XYZ2[0]))

print(len(matrix))
print(len(matrix[0]))


def f_min(X,p):
    plane_xyz = p[0:3]
    distance = (plane_xyz*X.T).sum(axis=1) + p[3]
    return distance / np.linalg.norm(plane_xyz)

def residuals(params, signal, X):
    return f_min(X, params)

from scipy.optimize import leastsq
sol = leastsq(residuals, p0, args=(None, XYZ))[0]

print "Solution: ", sol
print "Old Error: ", (f_min(XYZ, p0)**2).sum()
print "New Error: ", (f_min(XYZ, sol)**2).sum()


'''
numpy_matrix = np.asmatrix(matrix)

xyz = np.array(matrix)

#print(xyz)

# Inital guess of the plane
p0 = np.array([0.506645455682, -0.185724560275, -1.43998120646, 1.37626378129])

import numpy as np
from Geometry import Point, Line, Plane

def fitplane(XYZ):
[rows,npts] = XYZ.shape

if not rows == 3:
print XYZ.shape
 raise ('data is not 3D')
 return None
if npts <3:
 raise ('too few points to fit plane')
return None

# Set up constraint equations of the form AB = 0,
# where B is a column vector of the plane coefficients
# in the form  b(1)*X + b(2)*Y +b(3)*Z + b(4) = 0.
t = XYZ.T
p = (np.ones((npts,1)))
A = np.hstack([t,p])
if npts == 3: # Pad A with zeros
A = [A, np.zeros(1,4)]

[u, d, v] = np.linalg.svd(A)# Singular value decomposition.
#print v[3,:]
B = v[3,:];# Solution is last column of v.
nn = np.linalg.norm(B[0:3])
B = B / nn
plane = Plane(Point(B[0],B[1],B[2]),D=B[3])
return plane


x = np.array(range(map_size))
y = np.array(range(map_size))

A = np.column_stack((np.ones(x.size), x, y))
c,resid,rank,sigma = np.linalg.lstsq(A,numpy_matrix)

print resid

num = 0;
for i in range(500):
    for j in range(500):
        x_land =  i-int((lander_diameter/lander_footpad))
        y_land = j-int((lander_diameter/lander_footpad))
        
        if(x_land < 0 or y_land < 0):
            continue
        else:
            midpoint = [int(math.floor(x_land+(lander_diameter/2))),int(math.floor(y_land+(lander_diameter/2)))]
                
        print(midpoint)
        
        #p1 = [midpoint[0] ,midpoint[1] - lander_diameter/2]
        #p2 = [midpoint[0] + math.cos() , midpoit[1] - lander_diameter/2]
        #p3 = [midpoint[0] + , midpoint[1]]
                      
            


'''
