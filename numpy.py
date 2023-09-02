#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

#DATA FOR LINE 1 
x1= np.array([0, 1, 2, 3, 4, 5])
y1= np.array([0, 700, 200, 300, 400, 500])

#DATA FOR LINE 2
x2= np.array([0, 1, 2, 3, 4, 5])
y2= np.array([50, 20, 40, 20, 60, 70])

#DATA FOR LINE 3 
x3= np.array([0, 1, 2, 3, 4, 5])
y3= np.array([10, 20, 30, 40, 50, 60])

#DATA FOR LINE 4 
x4= np.array([0, 1, 2, 3, 4, 5])
y4= np.array([200, 4, 250, 550,450, 150])

#CREATING SUBPLOTS
fig, axs = plt.subplots(2, 2)

#PLOTTING LINE 1 
axs[0, 0].plot(x1, y1)
axs[0, 0].set_title('line1')

#PLOTTING LINE 2
axs[0, 1].plot(x2, y2)
axs[0, 1].set_title('line2')

#PLOTTING LINE 3 
axs[1, 0].plot(x3, y3)
axs[1, 0].set_title('line3')



#PLOTTING LINE 4 
axs[1, 1].plot(x4, y4)
axs[1, 1].set_title('line4')


# In[ ]:




