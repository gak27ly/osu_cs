#CS325-400 HW2
#Name: Yuan Li
#Email: liyu4@orgeonstate.edu	

#Stooge Sort: take a list of numbers, then sort the list
def stoogeSort(A,first, last):
	#print(len(A))

	if A[first] > A[last]:
		A[first], A[last] = A[last], A[first]

	if (last-first+1) > 2:
		oneThird = oneThird = (last - first +1)//3
		stoogeSort(A, first, last - oneThird)
		stoogeSort(A, first + oneThird, last)
		stoogeSort(A, first, last- oneThird)

	return

