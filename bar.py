import matplotlib.pyplot as plt
import numpy as np
 
#plot 1
x = np.array(["White","Black","Red"])
y = np.array([5,8,10])
plt.subplot(1,2,1)
plt.bar(x,y,color="g")

#plot2

y1 = np.array([400,350])
mylabel = ["Apples","Bananas"]
mycolors= ["Red","Yellow"]
plt.subplot(1,2,2)
plt.pie(y1, labels = mylabel, colors=mycolors)

plt.show()