import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import datetime
import string
from scipy.stats import linregress

import matplotlib 
matplotlib.rcParams.update({'font.size': 10, 'font.weight':'bold'})


# sampling stations
# ARA13B01, ARA13B17, ARA13B22, ARA13B23, ARA13B34, ARA13B42, ARA13B49, ARA13B55
# i = [0, 1, 2, 3, 4, 5, 6, 7]

print("i: index of file list")
i = int(input("i = "))

do_files =sorted(glob('/Users/jung-ok/work1/ARA13B/processed/Winkler/dissolved*.csv'))

cruise=do_files[i].split('/')[-1].split('.')[0][-8:-2]
st=do_files[i].split('/')[-1].split('.')[0][-2:]

### read *.csv file
do_table= pd.read_csv(do_files[i], index_col=None)
# print(do_table['Oxygen, Winkler [umol/kg]']-do_table['Oxygen, SBE 43 [umol/kg]'])

### normal data와 outlier 구분
# 'flag'
# -  normal data 0
# -  outlier     1
do_table['flag']=0

### 데이터 프레임 구분 : 'flag' 열 추가
# fo       : outlier 포함, 
fo=do_table[do_table['flag']==0]
# go       : outlier 제거
# if i==0:      
#    fo['flag'][16]=3
#    fo['flag'][17]=3  
# elif i==3:      
#    fo['flag'][8]=3    
# elif i==4:      
#    fo['flag'][20]=3
#    fo['flag'][21]=3           

go=fo[fo['flag']<=1]


### outliers 포함 회귀선
fo_dropna=fo.dropna(subset=['Oxygen, Winkler [umol/kg]'])
xval=fo_dropna[u'Oxygen, Winkler [umol/kg]']
yval=fo_dropna[u'Oxygen, SBE 43 [umol/kg]']
# print(len(xval), len(yval))
slope0, intercept0, rval0, pval0, std_err0 = linregress(xval,yval)

# ### outliers 제외 회귀선
# go_dropna=go.dropna(subset=['Oxygen, Winkler [umol/kg]'])
# xval=go_dropna[u'Oxygen, Winkler [umol/kg]']
# yval=go_dropna[u'Oxygen, SBE 43 [umol/kg]']
# slope, intercept, rval, pval, std_err = linregress(xval,yval)

# fo['fit[umol/kg]'] = np.nan
fo['fit[umol/kg]']=float(slope0)*fo[u'Oxygen, Winkler [umol/kg]']+float(intercept0)
### normal data 회귀선
# go['fit[umol/kg]'] = np.nan
# go['fit[umol/kg]']=float(slope)*go[u'Oxygen, Winkler [umol/kg]']+float(intercept)

##################################
print('plot of linear regression fit') 

if i==0:
    _dx1 =  -10 ; _dy1 = 32
    _dx2 = - 0 ; _dy2 = -1.6
elif i==1:
    _dx1 =  -58 ; _dy1 = 105
    _dx2 = - 0 ; _dy2 = -6.0
elif i==2:
    _dx1 =  -20 ; _dy1 = 82
    _dx2 = - 0 ; _dy2 = -5.0
elif i==3:
    _dx1 =  -23 ; _dy1 = 71
    _dx2 = - 0 ; _dy2 = -4.0
elif i==4:
    _dx1 =  -6 ; _dy1 = 90
    _dx2 = - 0 ; _dy2 = -4.2
elif i==5:
    _dx1 =  -58 ; _dy1 = 118
    _dx2 = - 0 ; _dy2 = -6.6
elif i==6:
    _dx1 =  -40 ; _dy1 = 112
    _dx2 = - 0 ; _dy2 = -6.4 
elif i==7:
    _dx1 =  -33 ; _dy1 = 80
    _dx2 = - 0 ; _dy2 = -5.1
    

### outliers를 포함 회귀선과 normal data만 포함 회귀선 한 그림에 넣기
# fo       : + marker 
#                normal+outlier green
#                outlier dark red
#            + 회귀선 red   
# go       : + 회귀선 blue  

# if (i==0) | (i==3)| (i==4):  
#     _fcol='red'  ; _tcol='red'
# else:
#     _fcol='blue' ; _tcol='blue'  

_fcol='blue' ; _tcol='blue'      




### figsize(가로, 세로) 그래프 사이즈
fig = plt.subplots(figsize=(7, 8))
ax1=plt.subplot(1,1,1)

### sort_values 'Oxygen, Winkler [umol/kg]' 오름차순 정렬
### marker, 모든 데이터, green
fo.sort_values(u'Oxygen, Winkler [umol/kg]').plot(y=u'Oxygen, SBE 43 [umol/kg]',x=u'Oxygen, Winkler [umol/kg]',
    marker='o',markeredgecolor='darkgreen', markerfacecolor='green',markersize=7,mew=0.5, alpha=0.5,\
    linestyle='',color='green',clip_on=False, zorder=100, ax=ax1, legend=False)
### fit line, 모든 데이터, red
fo.sort_values(u'Oxygen, Winkler [umol/kg]').plot(y=u'fit[umol/kg]',x=u'Oxygen, Winkler [umol/kg]',legend=False, 
#        marker='o',markeredgecolor='darkblue', markerfacecolor='blue',markersize=7,mew=0.5, alpha=0.3,\
    linestyle='-',color=_fcol,clip_on=False, zorder=100, ax=ax1)

# ### outlier     
# if (i==0) | (i==3)| (i==4):    
#     ### marker, outlier, darkred   
#     fo[fo['flag']==3].plot(y=u'Oxygen, SBE 43 [umol/kg]',x=u'Oxygen, Winkler [umol/kg]',legend=False, 
#         marker='o',markeredgecolor='darkred', markerfacecolor='red',markersize=7,mew=0.5, alpha=0.5,\
#         linestyle='',color='red', clip_on=False, zorder=100, ax=ax1)       
#     ### fit line, outlier 제외, blue   
#     go.sort_values(u'Oxygen, Winkler [umol/kg]').plot(y=u'fit[umol/kg]',x=u'Oxygen, Winkler [umol/kg]',legend=False, 
#     #        marker='o',markeredgecolor='darkblue', markerfacecolor='blue',markersize=7,mew=0.5, alpha=0.3,\
#         linestyle='-',color='blue',clip_on=False, zorder=100, ax=ax1)   

### 기울기, y절편, R-squred
# 폰트사이즈 12
x_pos = fo[u'Oxygen, Winkler [umol/kg]'].median() +_dx1
y_pos = fo[u'Oxygen, SBE 43 [umol/kg]'].median() + _dy1  
ax1.text(x_pos, y_pos, 'slope, intercept, R$^2$', color='gray', fontsize=12)   
ax1.text(x_pos, y_pos + _dy2,'%2.4f' % slope0 + ','+ '%2.4f' % intercept0 + ',' + '%2.4f' % rval0**2, color=_tcol, fontsize=12) 
# if (i==0) | (i==3)| (i==4):   
#  ax1.text(x_pos, y_pos + _dy2*2,'%2.4f' % slope + ','+ '%2.4f' % intercept + ',' + '%2.4f' % rval**2, color='blue', fontsize=12)          

### x축 이름, y축 이름
ax1.set_xlabel("O2 [$\mu$mol/kg], Winkler", weight = 'semibold')
ax1.set_ylabel("O2 [$\mu$mol/kg], SBE 43", weight = 'semibold')

file_name = '/Users/jung-ok/work1/ARA13B/plot/Winkler/'+'linear regression'+'_winkler_ctd_'+cruise+st+'.png'

plt.suptitle(cruise+st)   
plt.savefig(file_name) 
plt.show()

print(i)
print('Done')
##################################