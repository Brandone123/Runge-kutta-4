 n=100
 ti=0
 tf=100
 nn=1001
 T=np.linspace(ti,tf,nn)
 X=[1/2,3/8,0,1/8]
 for ii in range(1,3):
  for x in [0.1,0.9]:
   Y=Sol(ii,n,x,ti,tf,nn,X)
   plt.figure(figsize=(10,10))
   plt.clf() # Efface le contenu de la figure courante
   p1,=plt.plot(T,Y[0],label='Ignorant', linewidth=5)
   p2,=plt.plot(T,Y[1],label='$Spreader$', linewidth=5)
   p3,=plt.plot(T,Y[2],label=r'$Stifler 1$', linewidth=5)
   p4,=plt.plot(T,Y[3],label=r'$Stifler 2$', linewidth=5)
   plt.legend([p1, p2, p3, p4],
   [r'$\iota$',r'$s$',r'$r_{1}$',r'$r_{2}$'])
   Axes=plt.gca()
   #Axes.xaxis.set_ticks(T)
   Axx=plt.xlabel("Time")
   Axx.set_fontsize(16)
   Axy=plt.ylabel("Fraction of population ")
   Axy.set_fontsize(16)
   #plt.title(" ")
   
   plt.savefig(Dir+"ModelDynamics"+str(ii)+str(10*x)
   +".png")
   plt.savefig(Dir+"ModelDynamics"+str(ii)+str(10*x)
   +".pdf",format="pdf")
   plt.savefig(Dir+"ModelDynamics"+str(ii)+str(10*x)
   +".eps",format="eps")
