#mergeSort is takes an array and rearrange the array in sorted order
def mergeSort(arr):
	mergeSort1(arr,0,len(arr)-1)

def mergeSort1(arr,first,last):
	if first<last:
		mid = (first+last)//2
		mergeSort1(arr,first,mid)
		mergeSort1(arr,mid+1,last)
		merge(arr,first, mid+1, last)

def merge(arr,first,mid,last):
	L = arr[first:mid]
	R = arr[mid:last+1]
	i = j = 0
	L.append(9999999999)
	R.append(9999999999)
	#for i in range(len(L)):
	#	print(L[i])
	#for i in range(len(R)):
	#	print(R[i])

	for p in range(first,last+1):
		#print(i , j)
		if L[i] <= R[j]:
			arr[p] = L[i]
			i=i+1
		else:
			arr[p] = R[j]
			j=j+1



		