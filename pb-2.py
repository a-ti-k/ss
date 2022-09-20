import numpy as np
import matplotlib.pyplot as plot
plot.figure(figsize=(14,8))

x = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,6 ,5 ,4 ,3 ,2 ,1]
n =np.arange(-2,11)
plot.subplot(411)
plot.stem(n,x)
# here n-5
n1 =np.arange(3,16)
plot.subplot(412)
plot.stem(n1,x);
# here n+4
n2 =np.arange(-6,7)
plot.subplot(413)
plot.stem(n2,x);
m = np.arange(min(min(n1),min(n2)),max(max(n1),max(n2))+1);

y1=np.zeros(len(m))
y2=np.zeros(len(m))

li=list(m)
y1[li.index(n1[0]):li.index(n1[0])+len(n1)]=x
y2[li.index(n2[0]):li.index(n2[0])+len(n2)]=x

y=2*y1-3*y2
plot.subplot(414)
plot.stem(m,y)
plot.show()