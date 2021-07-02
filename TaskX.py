#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


A=[]
A=np.array(A)
for i in range(1001):
    x=round(np.random.uniform(-32768,32767),2)
    A = np.append(A, x)
print (A)


# In[4]:


f = open("test1.txt", "a")
for i in range(1001):
    f.write(str(A[i])+"\n")
f.close()

#open and read the file after the appending:
f = open("test1.txt", "r")
print(f.read())
f.close()


# In[ ]:




