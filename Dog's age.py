print("Hello")
a=int(input("Input a dog's age in human years : "))
if(a>0):
    if(a<=2):
        age=a*10.5
        print("Age of the Dog")
        print("The dog's age in dog's years is ",age)
    if((a-2)>=2):
        age=((a-2)*4)+21
        print("Age of the Dog")
        print("The dog's age in dog's years is ",age)
