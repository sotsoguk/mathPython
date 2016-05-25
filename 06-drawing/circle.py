"""
a growing circle
"""

from matplotlib import pyplot as plt  
from matplotlib import animation

def create_circle():
	circle = plt.Circle( (0,0), 0.05, fc='red', ec='green')
	return circle

def update_radius(i, circle):
	# add pulsation
	if i // 30 == 0:
		circle.radius = i * 0.5
	else:
		circle.radius = 15 - (i-30)*0.5
	return circle

def create_animation():
	# get ref for current figure
	fig = plt.gcf()
	# axes
	ax = plt.axes( xlim = (-10, 10), ylim = (-10, 10))
	ax.set_aspect('equal')
	circle = create_circle()
	ax.add_patch(circle)
	# reference for funcanimation is never used, but otherwise Garbage collection would kill it
	# first param of FARGS is frame number
	anim = animation.FuncAnimation(
		fig, update_radius, fargs=(circle,), frames = 60, interval = 50)
	plt.title('Circle Animation')
	plt.show()

if __name__ == '__main__':
	create_animation()

