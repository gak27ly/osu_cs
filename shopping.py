def shopping(N,W,P,weight):
	m = [[ 0 for w in range(W+1)] for i in range(N+1)]

	for i in range(N+1):
		for w in range(W+1):
			if i == 0 or w == 0:
				m[i][w] = 0
			elif weight[i-1] <= w: 
				m[i][w] = max(m[i-1][w-weight[i-1]] + P[i-1], m[i-1][w])
			else:
				m[i][w] = m[i-1][w]

	#backtracking
	# result = m[N][W]
	# w = W


	# for i in range (N,0,-1):
	# 	if result <=0:
	# 		break
	# 	if result == m[i-1][W]:			# if the result is from top
	# 		continue 

	# 	else:	
	# 		Items.append(i)
	# 		result = result - P[i-1]
	# 		w = w - weight[i-1]

	return m[N][W]






# p = [1,2,3,2,5]
# w = [1,1,1,2,5]
# n = len(p)
# family = [1,2,3,4,5,6,7,8,9,10]
# summary = 0
# for i in range(len(family)):
# 	summary += shopping(n,family[i],p,w)
# print(summary)

