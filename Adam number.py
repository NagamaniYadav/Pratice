a=int(input("Enter a number : "))
b=a
s=a*a
xxxxxxxxx
print("The square of the given number %d"%s)
Reverse = 0
while(s > 0):
    Reminder = s %10
    Reverse = (Reverse * 10) + Reminder
    s = s //10
print("\nReverse of entered sqaure number is = %d" %Reverse)
rev=Reverse
Reverse = 0
while(a > 0):
    Reminder = a %10
    Reverse = (Reverse*10) + Reminder
    a = a //10.
print("\nReverse of entered number is = %d" %Reverse)
r=Reverse**2
print("The square of the Reversed enter number  %d"%r)
if(r==rev):
    print("This is a Adam number %d"%b)
else:
    print("This is not a Adam number %d"%b)
