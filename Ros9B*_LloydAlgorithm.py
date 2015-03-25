"""
Problem

Given: Integers k and m followed by a set of points Data in m-dimensional space.

Return: A set Centers consisting of k points (centers) resulting from applying the 
Lloyd algorithm to Data and Centers, where the first k points from Data are selected as the first k centers.

"""

from scipy.spatial import distance
import sys



'''Functions'''

def dist(p1, p2):
	'''Trivial Wrapper Method to Find Euclidean Distance'''
	return distance.euclidean(p1,p2)

def findClosestCenter(datapoint, centers):
	'''Finds the Closest Center to a Datapoint'''
	minDist = sys.maxint
	minIndex = 0
	for i in xrange(len(centers)):

		if dist(datapoint, centers[i]) < minDist:

			minDist = dist(datapoint, centers[i])
			minIndex = i

	return centers[minIndex]

def centroid(data, m):

	sums = [0]*m
	for i in xrange(m):
		sums[i] = 0
		for j in xrange(len(data)):
			sums[i] += data[j][i]

		sums[i] = sums[i]/len(data)

	return sums

def findClusters(data, centers):
	clusters = {}

	for datapoint in data:
		center = findClosestCenter(datapoint, centers)

		clusters[center].append(datapoint)

	return clusters


def lloydAlgorithm(k, m, data):

	centers = []

	for i in xrange(k):
		centers.append(data[i])

	cluster = findClusters(data, centers)

	print cluster
		
	#while sorted(centers) != sorted(cluster.keys()):
		#cluster = findClusters(data,centers)








	

	
		



	



'''Input/Output'''

data = []

with open('Data/rosalind_9c.txt') as infile:

	k,m = map(int, infile.readline().strip().split())
	data.extend([map(float, line.strip().split()) for line in infile.readlines()])


lloydAlgorithm(k,m,data)



