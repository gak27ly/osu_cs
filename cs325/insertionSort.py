
# InsertionSort: takes an array parameter, then sort the array
def insertionSort(arr):
	for i in range(1,len(arr)):
		key = arr[i]
		j = i -1
		while key<arr[j] and j>=0:
			arr[j+1] = arr[j]   #move larger number back 
			j = j-1
		arr[j+1] = key          #put smallest number in the front


		
