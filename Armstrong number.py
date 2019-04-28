a=int(input("Enter the lower limit range : "))
b=int(input("Enter the upper limit range : "))
for i in range(a,b):
    rem = 0
    sum = 0
    i1=i
    while i>0:
	    rem=i%10
	    sum=sum+(rem*rem*rem)
	    i=i//10
    if(sum==i1):
	    print(i1)

