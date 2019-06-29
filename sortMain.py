
from insertionSort import insertionSort
from mergeSort import mergeSort


file = open("data.txt","r")
insert = open("insert.txt","w+")
merge = open("merge.txt","w+")

lines = file.readlines()

for line in lines:
	line = line.rstrip()
	numbers = line.split(' ')
	numbers = [int(i) for i in numbers]
	numbers = numbers[1:]
	print("Before inserttion sort:")
	print (numbers)
	insertionSort(numbers)
	print("After insertion sort:")
	numbers = [str(i) for i in numbers]
	print(numbers)
	insert.writelines(numbers)
	insert.write("\n")

for line in lines: 
	line = line.rstrip()
	numbers = line.split(' ')
	numbers = [int(i) for i in numbers]
	numbers = numbers[1:]
	print("Before merge sort:")
	print (numbers)
	mergeSort(numbers)
	print("After merge sort:")
	numbers = [str(i) for i in numbers]
	print(numbers)
	merge.writelines(numbers)
	merge.write("\n")


 




