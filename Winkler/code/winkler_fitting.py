#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Image
from glob import glob
import datetime
import string
from scipy.stats import linregress


# In[1]:


get_ipython().system('python --version')


# In[5]:


files =sorted(glob('/work1/ARA09B/raw_data/winkler/*ctd.txt_TRT'))
list(enumerate(files))


# In[6]:


#station 04, 20180807
i=0
# #station 09, 20180809
# i=1
# #station 25, 20180824
# i=2
fname = files[0]

f = open(fname, 'r')

lines = f.readlines()


# In[10]:


#station 04, bottle 25
lines[90:161]

#station 04, bottle 25
lines[102:160]


# In[21]:


# #station 04, bottle 81
# lines[164:237]

#station 04, bottle 81
lines[176:234]


# In[24]:


# #station 04, bottle 28
# lines[330:402]

#station 04, bottle 28
lines[342:400]


# In[26]:


# #station 04, bottle 55
# lines[406:478]

#station 04, bottle 55
lines[418:476]


# In[36]:


# #station 04, bottle 52
# lines[576:648]

#station 04, bottle 52
lines[588:646]


# In[31]:


# #station 04, bottle 24
# lines[744:814]

#station 04, bottle 24
lines[754:812]


# In[34]:


# #station 04, bottle 22
# lines[1092:1162]

#station 04, bottle 22
lines[1102:1160]


# In[34]:


# #station 04, bottle 2
# lines[1092:1162]

#station 04, bottle 22
lines[1102:1160]


# In[122]:


#### station 04
st=4;

# #bottle 25
# bo=25;p=102;q=160
# #bottle 81
# bo=81;p=176;q=234
# #bottle 28
# bo=28;p=342;q=400
# #bottle 55
# bo=55;p=418;q=476
# #bottle 52
# bo=52;p=588;q=646
# # bottle 24
# bo=24;p=754;q=812
# # bottle 22
# bo=22;p=1102;q=1160

nn=[[25,102,160],
[81,176,234],
[28,342,400],
[55,418,476],
[52,588,646],
[24,754,812],
[22,1102,1160]]

# print nn[0][0], nn[0][1], nn[0][2]

for i in np.arange(len(nn)):
        bo=nn[i][0]; p=nn[i][1]; q=nn[i][2]
#         print bo, p, q 
        folder='/work1/ARA09B/raw_data/winkler/overshoot/'
        gname='ctd_station'+str(st)+'_bottle'+str(bo)+'.txt'
        # gname='/work1/ARA08B/raw_data/DO/optode_station29_bottle83.txt'
        # print gname

        g = open(folder+gname, 'w')

        header='Elapsed Time, Titrant [uL], Current [uA], Total Count, Repeated Count\n'

        g.write(header)

        for line in lines[p:q]:
        #     print line
            g.write(line)

        g.close()


# In[123]:


ofiles =sorted(glob('/work1/ARA09B/raw_data/winkler/overshoot/*.txt'))
list(enumerate(ofiles))


# In[212]:


### station 04
# # bottle 22
# i=0
# oname=ofiles[i]
# bottle 24
# i=1
# oname=ofiles[i]
# # bottle 25
# i=2
# oname=ofiles[i]
# # bottle 28
# i=3
# oname=ofiles[i]
# # bottle 52
# i=4
# oname=ofiles[i]
# # bottle 55
# i=5
# oname=ofiles[i]
# bottle 81
i=6
oname=ofiles[i]

df = pd.read_csv(oname, index_col=3)
# df[:16]


# In[213]:


df


# In[57]:


list(df[df[u' Repeated Count']==2].index)[0]


# In[231]:


### station 04
# bottle 81
bo=81
a=18;b=23;c=23;d=-3
current1=np.array(df[u' Current [uA]'][a:b])
titrant1=np.array(df[u' Titrant [uL]'][a:b])
current2=np.array(df[u' Current [uA]'][c:d])
titrant2=np.array(df[u' Titrant [uL]'][c:d])
# print(current1)
# print(titrant1)


# In[205]:


### station 04
# bottle 55
bo=55
a=16;b=21;c=22;d=-3
current1=np.array(df[u' Current [uA]'][a:b])
titrant1=np.array(df[u' Titrant [uL]'][a:b])
current2=np.array(df[u' Current [uA]'][c:d])
titrant2=np.array(df[u' Titrant [uL]'][c:d])
# print(current1)
# print(titrant1)


# In[190]:


### station 04
# bottle 52
bo=52
a=16;b=23;c=23;d=-1
current1=np.array(df[u' Current [uA]'][a:b])
titrant1=np.array(df[u' Titrant [uL]'][a:b])
current2=np.array(df[u' Current [uA]'][c:d])
titrant2=np.array(df[u' Titrant [uL]'][c:d])
# print(current1)
# print(titrant1)


# In[179]:


### station 04
# bottle 28
bo=28
a=21;b=27;c=27;
current1=np.array(df[u' Current [uA]'][a:b])
titrant1=np.array(df[u' Titrant [uL]'][a:b])
current2=np.array(df[u' Current [uA]'][c:])
titrant2=np.array(df[u' Titrant [uL]'][c:])
# print(current1)
# print(titrant1)


# In[147]:


### station 04
# bottle 25
bo=25
a=18;b=23;c=23;d=-1
current1=np.array(df[u' Current [uA]'][a:b])
titrant1=np.array(df[u' Titrant [uL]'][a:b])
current2=np.array(df[u' Current [uA]'][c:d])
titrant2=np.array(df[u' Titrant [uL]'][c:d])
# print(current1)
# print(titrant1)


# In[135]:


### station 04
# bottle 24
bo=24
a=16;b=25;c=25;d=-1
current1=np.array(df[u' Current [uA]'][a:b])
titrant1=np.array(df[u' Titrant [uL]'][a:b])
current2=np.array(df[u' Current [uA]'][c:d])
titrant2=np.array(df[u' Titrant [uL]'][c:d])
# print(current1)
# print(titrant1)


# In[126]:


### station 04
# bottle 22
a=16;b=23;c=25;
current1=np.array(df[u' Current [uA]'][a:b])
titrant1=np.array(df[u' Titrant [uL]'][a:b])
current2=np.array(df[u' Current [uA]'][c:])
titrant2=np.array(df[u' Titrant [uL]'][c:])
# print(current1)
# print(titrant1)


# In[233]:


get_ipython().run_line_magic('matplotlib', '')
fig, ax = plt.subplots()
ax.plot(titrant1, current1, linestyle='-', marker='o')
ax.plot(titrant2, current2, linestyle='-', marker='o')
plt.show()


# In[234]:


### station 04
# bottle 81
x_axis1=df[a:b][u' Titrant [uL]']
y_axis1=df[a:b][u' Current [uA]']
slope1, intercept1, r_value1, p_value1, std_err1 = linregress(x_axis1,y_axis1)

slope1='%4.6f' % slope1
intercept1='%4.6f' % intercept1
r_value1='%4.6f' % r_value1
print(slope1, intercept1, r_value1)

### station 04
# bottle 24
x_axis2=df[c:][u' Titrant [uL]']
y_axis2=df[c:][u' Current [uA]']
slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x_axis2,y_axis2)

slope2='%4.6f' % slope2
intercept2='%4.6f' % intercept2
r_value2='%4.6f' % r_value2
print(slope2, intercept2, r_value2)


End_Point =  (float(intercept2)-float(intercept1))/(float(slope1)-float(slope2))
# type(slope1)
print(End_Point)


# In[207]:


### station 04
# bottle 55
x_axis1=df[a:b][u' Titrant [uL]']
y_axis1=df[a:b][u' Current [uA]']
slope1, intercept1, r_value1, p_value1, std_err1 = linregress(x_axis1,y_axis1)

slope1='%4.6f' % slope1
intercept1='%4.6f' % intercept1
r_value1='%4.6f' % r_value1
print(slope1, intercept1, r_value1)

### station 04
# bottle 24
x_axis2=df[c:][u' Titrant [uL]']
y_axis2=df[c:][u' Current [uA]']
slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x_axis2,y_axis2)

slope2='%4.6f' % slope2
intercept2='%4.6f' % intercept2
r_value2='%4.6f' % r_value2
print(slope2, intercept2, r_value2)


End_Point =  (float(intercept2)-float(intercept1))/(float(slope1)-float(slope2))
# type(slope1)
print(End_Point)


# In[193]:


### station 04
# bottle 52
x_axis1=df[a:b][u' Titrant [uL]']
y_axis1=df[a:b][u' Current [uA]']
slope1, intercept1, r_value1, p_value1, std_err1 = linregress(x_axis1,y_axis1)

slope1='%4.6f' % slope1
intercept1='%4.6f' % intercept1
r_value1='%4.6f' % r_value1
print(slope1, intercept1, r_value1)

### station 04
# bottle 24
x_axis2=df[c:][u' Titrant [uL]']
y_axis2=df[c:][u' Current [uA]']
slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x_axis2,y_axis2)

slope2='%4.6f' % slope2
intercept2='%4.6f' % intercept2
r_value2='%4.6f' % r_value2
print(slope2, intercept2, r_value2)


End_Point =  (float(intercept2)-float(intercept1))/(float(slope1)-float(slope2))
# type(slope1)
print(End_Point)


# In[181]:


### station 04
# bottle 28
x_axis1=df[a:b][u' Titrant [uL]']
y_axis1=df[a:b][u' Current [uA]']
slope1, intercept1, r_value1, p_value1, std_err1 = linregress(x_axis1,y_axis1)

slope1='%4.6f' % slope1
intercept1='%4.6f' % intercept1
r_value1='%4.6f' % r_value1
print(slope1, intercept1, r_value1)

### station 04
# bottle 24
x_axis2=df[c:][u' Titrant [uL]']
y_axis2=df[c:][u' Current [uA]']
slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x_axis2,y_axis2)

slope2='%4.6f' % slope2
intercept2='%4.6f' % intercept2
r_value2='%4.6f' % r_value2
print(slope2, intercept2, r_value2)


End_Point =  (float(intercept2)-float(intercept1))/(float(slope1)-float(slope2))
# type(slope1)
print(End_Point)


# In[149]:


### station 04
# bottle 25
x_axis1=df[a:b][u' Titrant [uL]']
y_axis1=df[a:b][u' Current [uA]']
slope1, intercept1, r_value1, p_value1, std_err1 = linregress(x_axis1,y_axis1)

slope1='%4.6f' % slope1
intercept1='%4.6f' % intercept1
r_value1='%4.6f' % r_value1
print(slope1, intercept1, r_value1)

### station 04
# bottle 24
x_axis2=df[c:][u' Titrant [uL]']
y_axis2=df[c:][u' Current [uA]']
slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x_axis2,y_axis2)

slope2='%4.6f' % slope2
intercept2='%4.6f' % intercept2
r_value2='%4.6f' % r_value2
print(slope2, intercept2, r_value2)


End_Point =  (float(intercept2)-float(intercept1))/(float(slope1)-float(slope2))
# type(slope1)
print(End_Point)


# In[138]:


### station 04
# bottle 24
x_axis1=df[a:b][u' Titrant [uL]']
y_axis1=df[a:b][u' Current [uA]']
slope1, intercept1, r_value1, p_value1, std_err1 = linregress(x_axis1,y_axis1)

slope1='%4.6f' % slope1
intercept1='%4.6f' % intercept1
r_value1='%4.6f' % r_value1
print(slope1, intercept1, r_value1)

### station 04
# bottle 24
x_axis2=df[c:][u' Titrant [uL]']
y_axis2=df[c:][u' Current [uA]']
slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x_axis2,y_axis2)

slope2='%4.6f' % slope2
intercept2='%4.6f' % intercept2
r_value2='%4.6f' % r_value2
print(slope2, intercept2, r_value2)


End_Point =  (float(intercept2)-float(intercept1))/(float(slope1)-float(slope2))
# type(slope1)
print(End_Point)


# In[137]:


### station 04
# bottle 22
x_axis1=df[a:b][u' Titrant [uL]']
y_axis1=df[a:b][u' Current [uA]']
slope1, intercept1, r_value1, p_value1, std_err1 = linregress(x_axis1,y_axis1)

slope1='%4.6f' % slope1
intercept1='%4.6f' % intercept1
r_value1='%4.6f' % r_value1
print(slope1, intercept1, r_value1)

### station 04
# bottle 22
x_axis2=df[c:][u' Titrant [uL]']
y_axis2=df[c:][u' Current [uA]']
slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x_axis2,y_axis2)

slope2='%4.6f' % slope2
intercept2='%4.6f' % intercept2
r_value2='%4.6f' % r_value2
print(slope2, intercept2, r_value2)

End_Point =  (float(intercept2)-float(intercept1))/(float(slope1)-float(slope2))
# type(slope1)
print(End_Point)


# In[235]:


df['fit1 [uA]'] = np.nan
df['fit2 [uA]'] = np.nan

df['fit1 [uA]']=float(slope1)*df[u' Titrant [uL]']+float(intercept1)
df['fit2 [uA]']=float(slope2)*df[u' Titrant [uL]']+float(intercept2)


# In[236]:


df


# In[237]:


get_ipython().run_line_magic('matplotlib', '')
fig = plt.subplots(figsize=(8, 8))
ax1=plt.subplot(1,1,1);
df[a:].plot(y=u' Current [uA]',x=u' Titrant [uL]',legend=False, linestyle='--',            marker='o', ax=ax1)
df[a:].plot(y=u'fit1 [uA]',x=u' Titrant [uL]',legend=False, linestyle='-',            marker='o', ax=ax1)
df[a:].plot(y=u'fit2 [uA]',x=u' Titrant [uL]',legend=False, linestyle='-',            marker='o', ax=ax1)
plt.show()


# In[238]:


print st,',', bo,',', "{0:.2f}".format(End_Point)
# print float("{0:.2f}".format(End_Point))


# In[115]:


## [bottle #, end point]
hand=[[22, 1259.73],
[24, 1140.61],
[25 , 1238.82], 
[28 , 1205.78],
[52 , 1063.72],
[55 , 1178.19],
[81 , 1283.34]]

