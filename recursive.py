def factorial(x):
 if x==1:
     return(1)
 else:
    return(x*factorial(x-1))
a=int(input("enter a number "));
if(a>=1):
 print("factorial of a number",factorial(a)) 
