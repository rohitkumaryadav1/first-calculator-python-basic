#making first calculator
#take input from user
print("*************rohit calculator***************************")
w=str(input("what you want to do \na)addition\nb)substraction\nc)multiplication\nd)division\n="))
x=int(input("enter first number="))
y=int(input("enter second number="))
 #now we rund the oberation based on the user input

if (w=="a"):
    print(x+y)
elif (w=="b"):
    print(x-y)
elif (w=="c"):
    print(x*y)
elif (w=="d"):
    print(x/y)
else:
  print("we have only 4 operation given above as option a,b,c,d") 