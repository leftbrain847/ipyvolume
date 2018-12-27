
# coding: utf-8

# In[72]:


import csv

with open('margin.csv', 'rU') as p:
    reader = csv.reader(p)
    margin = ([list(map(float,rec)) for rec in csv.reader(p, delimiter=',')])

with open('gp.csv', 'rU') as p:
    reader = csv.reader(p)
    gp = ([list(map(float,rec)) for rec in csv.reader(p, delimiter=',')])
    
with open('spread_to_const.csv', 'rU') as p:
    reader = csv.reader(p)
    spread_to_const = ([list(map(float,rec)) for rec in csv.reader(p, delimiter=',')])


# In[73]:


import ipyvolume as ipv
import numpy as np
import ipywidgets as widgets
from ipyvolume.widgets import quickscatter
from ipyvolume.widgets import Figure
import numpy as np, pandas as pd; np.random.seed(0)
import seaborn as sns; sns.set(style="white", color_codes=True)


# In[74]:


x = np.array(margin)
y = np.array(gp)
z = np.array(spread_to_const)


# In[76]:


ipv.figure()
s = ipv.scatter(x, y, z, marker='sphere',  size=2)

ipv.pylab.xlabel('Margin')
ipv.pylab.ylabel('GP')
ipv.pylab.zlabel('Var to Const')

ipv.animation_control(s) # shows controls for animation controls
ipv.show()

