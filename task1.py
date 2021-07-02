#!/usr/bin/env python
# coding: utf-8

# In[47]:


import numpy as np


# In[48]:


def main(): 
    f = open("test1.txt", "r")
    A=f.readlines()
    string_series = A

    floats_list = []
    for item in string_series:
        floats_list.append(float(item))
    A=np.array(A)
    B=floats_list
    B=np.array(B)
    print (round((np.nanpercentile(B,90)),2))
    print (round((np.median(B)),2))
    print (np.max(B))
    print (np.min(B))
    print (round((np.mean(B)),2))
    f.close()
if __name__== "__main__":

    main()


# In[ ]:




