import numpy as np 
import matplotlib.pyplot as plt 
from random import randint
import math

def rand_cluster(K):
	clusters = []
	for i in range(K):
		cluster_pos = [randint(0,255), randint(0,255), randint(0,255)] #random cluster position 
		clusters.append(cluster_pos)
	return clusters

def calc_distance(p1, p2):
	dimension = len(p1) 
	distance = 0
	for i in range(dimension):
		distance += (p1[i] - p2[i])**2
	return math.sqrt(distance)

def main():
	image = plt.imread("sunflower.jpg") # (656, 561, 3)

	height = image.shape[0] #rows 
	width = image.shape[1]	#columns

	image = image.reshape(height*width, 3) # -> pixel pos 

	#change K here
	K = 4
	clusters = rand_cluster(K) # -> postion of each cluster
	labels = []
	
	# calculate distance 
	for p in image:
		distances = []
		for c in clusters: 
			distance = calc_distance(p, c)
			distances.append(distance)

		min_distance = min(distances) #find min distance
		#find index to assign label
		idx_min = distances.index(min_distance)# -> 0/1/...
		labels.append(idx_min) #assign label

	for i in range(K):
		sum_x = 0 
		sum_y = 0
		sum_z = 0
		point_count = 0 
		for j in range(len(image)):
			if i == labels[j]:
				sum_x += image[j][0]
				sum_y += image[j][1]
				sum_z += image[j][2]
				point_count += 1
		if point_count != 0:
			#new pos = average pos
			new_x = sum_x/point_count 
			new_y = sum_y/point_count
			new_z = sum_z/point_count
			clusters[i] = [new_x, new_y, new_z] #update position

	new_image = np.zeros((height,width,3), dtype=np.uint8)

	pixel_index = 0
	for i in range(height):
		for j in range(width):
			label_of_pixel = labels[pixel_index]
			new_image[i][j] = clusters[label_of_pixel]
			pixel_index += 1

	plt.imshow(new_image)
	plt.show()
main()
