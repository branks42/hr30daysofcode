#Intro to Conditional Statements

N = int(input().strip())

if N % 2 ==1:
	print("Weird")
else:
	if N % 2 == 0 and N > 20:
		print("Not Weird")
	elif N % 2 ==0 and 2 <= N <=5:
		print ("Not Weird")
	elif N % 2 ==0 and 6 <= N <= 20:
		print ("Weird")

# END #