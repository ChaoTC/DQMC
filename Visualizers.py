# import plotly.plotly as py
# import plotly.graph_objs as go
import matplotlib.pyplot as plt
import numpy as np

class Visualizer2D(object):

	@staticmethod
	def visualize(title, distribution, length, stepLength):
		y, x = np.mgrid[slice(-length/2, length/2 + stepLength, stepLength), slice(-length/2, length/2 + stepLength, stepLength)]
		z = (distribution)
		z_min, z_max = 0, np.abs(z).max()

		plt.pcolor(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
		plt.title(title)
		# set the limits of the plot to the limits of the data
		plt.axis([x.min(), x.max(), y.min(), y.max()])
		plt.colorbar()
		plt.show()
		# trace = go.Heatmap(z = distribution)
		# data = [trace]
		# py.iplot(data, filename = 'heatmap')

class Visualizer3D(object):

	@staticmethod
	def visualize(title, distribution, length, stepLength):
		steps = length/stepLength
		z=0
		while(z<steps):
			y, x = np.mgrid[slice(-length/2, length/2 + stepLength, stepLength), slice(-length/2, length/2 + stepLength, stepLength)]
			t = (distribution[:,:,z])
			t_min, t_max = 0, np.abs(z).max()

			plt.pcolor(x, y, t, cmap='RdBu', vmin=t_min, vmax=t_max)
			plt.title(title)
			# set the limits of the plot to the limits of the data
			plt.axis([x.min(), x.max(), y.min(), y.max()])
			plt.colorbar()
			plt.show()
			z+=5