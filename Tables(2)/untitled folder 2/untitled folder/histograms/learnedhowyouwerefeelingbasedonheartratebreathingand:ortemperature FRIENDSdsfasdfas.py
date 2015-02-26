
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

def parse(text):
	f = open(text,'r')
	line = f.readline()
	prev = None
	combined = []

	while line:
		x = line.split()
		if prev != None and prev != x[0]:
			plt.hist(edgecolor = "none",x = combined,color = 'green',bins = range(0,7),alpha = 0.5, align = 'mid', rwidth = 1)
		# plt.tick_params(\
  #   axis='x',          # changes apply to the x-axis
  #   which='both',      # both major and minor ticks are affected
  #   bottom='off',      # ticks along the bottom edge are off
  #   top='off',         # ticks along the top edge are off
  #   labelbottom='off') # labels along the bottom edge are off
		#plt.xticks(np.arange(1,6))
			plt.xticks([])
			plt.yticks([])
			plt.axis('off')


			savefig(str(prev) + " combined", dpi=None, facecolor='w', edgecolor='w',
			orientation='portrait', papertype=None, format=None,
			transparent=False, bbox_inches='tight', pad_inches=0,
			frameon=None)
			combined = []
			plt.clf()
		prev = x[0]

		numbers = list(x[2])

		title = str(x[0])+ " " + str(x[1])
		for i in range(len(numbers)):
			numbers[i] = int(numbers[i])
			combined.append(numbers[i])
		plt.hist(edgecolor = "none",x = numbers,color = 'green',bins = range(0,7),alpha = 0.5, align = 'mid', rwidth = 1)
		# plt.tick_params(\
  #   axis='x',          # changes apply to the x-axis
  #   which='both',      # both major and minor ticks are affected
  #   bottom='off',      # ticks along the bottom edge are off
  #   top='off',         # ticks along the top edge are off
  #   labelbottom='off') # labels along the bottom edge are off
		#plt.xticks(np.arange(1,6))
		plt.xticks([])
		plt.yticks([])
		plt.axis('off')

		savefig(title, dpi=None, facecolor='w', edgecolor='w',
		orientation='portrait', papertype=None, format=None,
		transparent=False, bbox_inches='tight', pad_inches=0,
		frameon=None)
		line = f.readline()
		plt.clf()


	
parse("file.txt")
