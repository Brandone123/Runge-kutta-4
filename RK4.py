 from math import *
 from matplotlib import pyplot as plt
 
 def p(i=1,n=10,k=1,x=0.1):
  if i==1:
   res=factorial(n-2)/(factorial(k-1)*factorial(n-k-1))
   res*=pow(x,k-1)*pow(1-x,n-k-1)
  if i==2:
   if (x>0):
    res=x*(pow(1-x,k-1))/(1-pow(1-x,n-1))
   else:
    res=(k-1)/(n-1)
  if i==3:
   res=0
   if (x>0):
    for j in range(1,n):
     temp=factorial(k-1)/factorial(j-1);
     res+=temp*pow(x,j-k);
    res=1/res
  return res
 
 def phi(ii=1,n=10,x=0.1,i=0.25):
  res=p(ii,n,1,x)
  for k in range(2,n):
   res+=p(ii,n,k,x)*pow(i,k-1)/k
  return res
