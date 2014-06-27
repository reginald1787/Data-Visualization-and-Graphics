import matplotlib.pyplot as plt
from pylab import figure, show, rand
from matplotlib.patches import Ellipse

def drawEllipse(data):
	# useful for drawing Gaussians
	# parameters: center, width, height, angle 
	# center is mean of Gaussian, width, height are the eigenvalues of covariance matrix
	# angle could be calculated by the corresponding eigenvectors
	
	# data is a list of Gaussian mixtures
	# each element could have multiple Gaussians
	
	fig = figure()
	ax = fig.add_subplot(111, aspect='equal')
	
	# set color in the form of (R,G,B)
	# set all the colors in the same illumination 
	
	colors = [(a,b,c) for a,b,c in zip(rand(len(data)),rand(len(data)),rand(len(data)))]
	colors = [c/sum(c) for c in colors]
	
	for j in range(len(data)):
		m = data[j][0			# mean 
		w = data[j][1]			# weight
		c = data[j][2]			# covariance
		for i in range(len(m)):
			mean = m[i]
			weight = w[i]
			cov = c[i]
			v, x = np.linalg.eigh(cov)
			angle = np.arctan2(x[0][1], x[0][0])
			angle = 180 * angle / np.pi  # convert to degrees
			v /= np.linalg.norm(v)
			v *=40
	
			if j==img:
				facecolor = colors[j]
			else:
				facecolor = 'None'
			
			# draw ellipse with different edge color and face color
			ell = Ellipse(mean, v[0], v[1], 180 + angle, edgecolor=colors[j],fc=facecolor)
			
			# set the transparency 
			ell.set_alpha(alpha[j])
			
			ax.add_artist(ell)
	
	# set the x,y axis
	ax.set_xlim(0, 200)
	ax.set_ylim(0, 150)
	
	# plot single points
	for p in pts:
		ax.plot(p[0],p[1],'*',color='b')
		
	plt.hold(True)	
	show()
