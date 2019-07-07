#CS325-400 HW2
#Name: Yuan Li
#Email: liyu4@orgeonstate.edu	
import random
import time
from stoogeSort import stoogeSort

for n in range(100, 1100, 100):
	print("The size of the array is %d" %n)
	total = 0
	for j in range(3):
		seconds = 0
		arr = [0]*n
		for i in range(n):
			arr[i] = random.randint(0,10000)
		start = time.clock()
		stoogeSort(arr,0,len(arr)-1)
		seconds = time.clock() - start
		total = seconds + total
	print("The time for stooge Sort is : %f" %(total/3))

