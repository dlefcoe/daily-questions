# imports
import time
import numpy as np 
import matplotlib.pyplot as plt 
from numpy.linalg import norm 

# gravity
g = 9.8

# masses
m_1 = 10
m_2 = 20
m_3 = 30

# starting coordinates
p1_start = np.array([-10, 10, -11])
v1_start = np.array([-3, 0, 0])

p2_start = np.array([0, 0, 0])
v2_start = np.array([0, 0, 0])

p3_start = np.array([10, 10, 12])
v3_start = np.array([3, 0, 0])



def accelerations(p1, p2, p3):
	"""
	A function to calculate the derivatives of x, y, and z
	given 3 object and their locations according to Newton's laws
	"""
	p_1_dv = -g * (m_2 * (p1 - p2)/(norm(p1-p2)**3)
		       	+ m_3 * (p1 - p3)/(norm(p1-p3)**3))

	p_2_dv = -g * (m_3 * (p2 - p3)/(norm(p2-p3)**3)
		       	+ m_1 * (p2 - p1)/(norm(p2-p1)**3))

	p_3_dv = -g * (m_1 * (p3 - p1)/(norm(p3-p1)**3)
		      	+ m_2 * (p3 - p2)/(norm(p3-p1)**3))

	return p_1_dv, p_2_dv, p_3_dv


# parameters
delta_t = 0.01
steps = 10_000

t0 = time.time()
# initialize trajectory array
p1 = np.array([[0.,0.,0.] for i in range(steps)])
v1 = np.array([[0.,0.,0.] for i in range(steps)])

p2 = np.array([[0.,0.,0.] for i in range(steps)])
v2 = np.array([[0.,0.,0.] for i in range(steps)])

p3 = np.array([[0.,0.,0.] for i in range(steps)])
v3 = np.array([[0.,0.,0.] for i in range(steps)])
t1 = time.time()
print('time taken:', round(t1-t0, 1), 'seconds')

# starting point and velocity
p1[0], p2[0], p3[0] = p1_start, p2_start, p3_start
v1[0], v2[0], v3[0] = v1_start, v2_start, v3_start



# evolution of the system
for i in range(steps-1):
	# calculate derivatives
	dv1, dv2, dv3 = accelerations(p1[i], p2[i], p3[i])

	v1[i + 1] = v1[i] + dv1 * delta_t
	v2[i + 1] = v2[i] + dv2 * delta_t
	v3[i + 1] = v3[i] + dv3 * delta_t

	p1[i + 1] = p1[i] + v1[i] * delta_t
	p2[i + 1] = p2[i] + v2[i] * delta_t
	p3[i + 1] = p3[i] + v3[i] * delta_t

t2 = time.time()
print('time taken:', round(t2-t1, 1), 'seconds')


# plot the chart
ax = plt.figure().add_subplot(projection='3d')

plt.plot([i[0] for i in p1], [j[1] for j in p1], [k[2] for k in p1] ,
			'.', color='red', lw = 0.05, markersize = 0.1)
plt.plot([i[0] for i in p2], [j[1] for j in p2], [k[2] for k in p2] , 
			'.', color='green', lw = 0.05, markersize = 0.1)
plt.plot([i[0] for i in p3], [j[1] for j in p3], [k[2] for k in p3] , 
			'.', color='blue', lw = 0.05, markersize = 0.1)

ax.set_xlabel('X --->')
ax.set_ylabel('Y --->')
ax.set_zlabel('Z --->')

plt.show()
