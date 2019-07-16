from shopping import shopping

f = open("shopping.txt","r")
r = open("results.txt","w+")


R = f.readline()
R = int(R)

for i in range(R):
	r.write('Test case %s\n' % str(i+1)) 
	items = f.readline()
	items = int(items)
	summary = 0

	P = []				#list for price
	W = []				#list for weight

	for j in range(items):
		p,w = f.readline().split()
		P.append(int(p))
		W.append(int(w))

	family = int(f.readline())
	F = [] 				#list for family members
	for k in range(family):
		member = int(f.readline())
		F.append(member)


	n = len(P)

	for p in range(len(F)):
		summary += shopping(n,F[p],P,W)
	r.write('Total Price %s\n' %str(summary))	

	








