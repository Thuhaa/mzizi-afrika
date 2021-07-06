def findnumbers(arr, k):
	for i in range(0, len(arr)):
		if arr[i] == k and k != 0:
			print("YES")
		else:
			print("NO")
arr = [1,2,3,4,5]
k = 5
findnumbers(arr, k)