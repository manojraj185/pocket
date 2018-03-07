#Author : Manoj R

import numpy as np
import pandas as pd
import random

alpha = 0.1
mina = 2000
minw = []
def isValid(prod1,label, rows, w) :
	global mina
	global minw
	prod = prod1[0]
	a = []
	for i in range(0,rows,1):
		if (prod[i] >= 0) and (label[i] == 1):
			continue
		elif (prod[i] < 0) and (label[i] == -1):
			continue
		else:
			a.append(i)
	if len(a) > 0 :
		if mina > len(a) :
			mina = len(a)
			minw = w
		ind = random.randrange(0,len(a))
		return a[ind]
	return -1

def pocket(data, label, rows):
	a = []
	for i in range(0,3) :
		#a.append(random.uniform(-1,1))
		a.append(0)
	w = np.array([a])
	count = 0
	#print w.T
	#print data.T
	prod = np.dot(w, data.T)
	index = isValid(prod, label, rows, w)
	while (index != -1) and count < 100:
		term = np.dot(w, data[index].T)
		if (label[index] == 1) and prod[0][index] < 0:
			while term[0] < 0:
				w = w + alpha*(data[index])
				term = np.dot(w, data[index].T)
		else:
			while term[0] >= 0:
				w = w - alpha*(data[index])
				term = np.dot(w, data[index].T)
		count  = count + 1
		prod = np.dot(w, data.T)
		index = isValid(prod, label, rows, w)
	return

if __name__ == '__main__':
	df = pd.read_csv('classification.txt', sep = ",", header = None)
	rows = df[0].count()
	df1 = df.iloc[0:rows,0:3]
	df2 = pd.DataFrame(1, index = range(rows), columns = range(1))
	frames = [df2,df1]
	df3 = pd.concat(frames)
	#print df1
	labels = df[3]
	#print labels
	pocket(df1.as_matrix(), labels, rows)
