 def F(ii=1,n=10,x=0.1,X=[1/2,1/4,0,1/4]):
  beta=[0.1,0.1,0.1]
  alpha=0.1
  delta=0.1
  res=[]
  temp=-X[0]*phi(ii,n,x,X[0])*(beta[0]*X[1]+beta[1]*X[3])
  res.append(temp)
  temp=X[1]*phi(ii,n,x,X[0])*(beta[0]*X[0]-beta[2]*X[3])
  res.append(temp)
  temp=X[3]*phi(ii,n,x,X[0])*(beta[1]*X[0]+beta[2]*X[1])
  temp+=-alpha*X[2]+delta*X[3]
  res.append(temp)
  temp+=alpha*X[2]-delta*X[3]
  res.append(temp)
  return res
 
 def Sol(ii=1,n=100,x=0.1,ti=0,tf=10,nn=11,
  X=[1/2,3/8,0,1/8]):
  h=(tf-ti)/(nn-1)
  res=[X]
  for i in range(nn-1):
   tmp=F(ii,n,x,res[-1])
   k1=[h*tmp[j] for j in range(4)]
   tmp=[res[-1][j]+k1[j]/2 for j in range(4)]
   tmp=F(ii,n,x,tmp)
   k2=[h*tmp[j] for j in range(4)]
   tmp=[res[-1][j]+k2[j]/2 for j in range(4)]
   tmp=F(ii,n,x,tmp)
   k3=[h*tmp[j] for j in range(4)]
   tmp=[res[-1][j]+k3[j] for j in range(4)]
   tmp=F(ii,n,x,tmp)
   k4=[h*tmp[j] for j in range(4)]
   tmp=[res[-1][j]+(k1[j]+2*k2[j]+2*k3[j]+k4[j])
   for j in range(4)] res.append(tmp)
  resBis=[[res[i][j] for i in range(len(res))]
  for j in range(4)]
  return resBis
