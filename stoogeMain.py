from stoogeSort import stoogeSort

file = open("data.txt","r")
stooge = open("stooge.txt","w+")

lines = file.readlines()

for line in lines:
	line = line.strip()
	numbers = line.split(' ')
	numbers = numbers[1:]
	numbers = [int(i) for i in numbers]
	print("Before stooge sort:")
	print (numbers)
	stoogeSort(numbers,0,len(numbers)-1)
	print("After stooge sort:")
	print(numbers)
	numbers = [str(i) for i in numbers]
	for i in numbers:
		stooge.write(i+' ')
	stooge.write('\n')

file.close()
stooge.close()

