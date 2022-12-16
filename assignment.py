import numpy as np
import matplotlib.pyplot as plt
y1=np.fromfile("C:/sales/1year.txt",dtype=int,sep=",")
y2=np.fromfile("C:/sales/2year.txt",dtype=int,sep=",")
s1=np.fromfile("C:/sales/1sales.txt",dtype=int,sep=",")
s2=np.fromfile("C:/sales/2sales.txt",dtype=int,sep=",")
plt.plot(y1,s1,label="sales-1")
plt.plot(y2,s2,label="sales-2")
plt.legend(loc="upper right")
plt.ylabel("sales")
plt.xlabel("years")
plt.show()ny