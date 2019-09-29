import random
import time
from insertionSort import insertionSort

f = open("insertTime.text","w+")

total = 0

for n in range(1000,11000,1000):
	print("The size of the array is %d" %n)
	arr = [0]* n;
	for i in range(n):
		arr[i] = random.randint(0,10000)

	start = time.clock()
	insertionSort(arr)
	seconds = time.clock() - start
	print("The time for insertion Sort is : %f" %seconds)
	total = total + seconds
	seconds = str(seconds)
	f.write(seconds+'\n')

f.close()