import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import datetime
import string
from scipy.stats import linregress

### plotting
import matplotlib 
matplotlib.rcParams.update({'font.size': 10, 'font.weight':'bold'})

def plot_depth_profile_winkler_ctd(st, dw, dc, ymin, ymax):
    # fig, ax1 = plt.subplots(figsize=(9, 9))
    fig = plt.figure(figsize=(6, 9))
    ax1= fig.add_axes([0.15, 0.1, 0.8, 0.7]) 

    dw.plot(y=u'Depth',x='O2[umol/kg]', legend=True,  ax=ax1, \
 marker='o',mec='darkblue', mfc='blue', ms=7, mew=0.5, alpha=0.5, ls='', clip_on=False, zorder=100, label='Winkler')
    dc.plot(y='Depth',x='O2[umol/kg]', legend=True,  ax=ax1, \
 marker='o',mec='darkred', mfc='red', ms=7, mew=0.5, alpha=0.5, ls='', clip_on=False, zorder=100, label='CTD')

    ax1.set_ylim(ymax,ymin)
    ax1.set_xlabel('O2 [umol/kg]', fontsize=10, weight = 'semibold', color='black')#color='green'
    ax1.set_ylabel('Depth [m]', fontsize=10, weight = 'semibold')
    ax1.set_title('Station '+str(st)+',  ARA13B')
    folder='/Users/jung-ok/work1/ARA13B/plot/Winkler/'
    fname='Depth_profile_Winkler_CTD_st'+str(st)+'.png'
    plt.savefig(folder+fname) 
    plt.show()

def plot_lr_winkler_ctd(cruise, st, slope0, intercept0, rval0, rc):
    fig = plt.figure(figsize=(7, 8))
    ax1= fig.add_axes([0.15, 0.1, 0.8, 0.7]) 
    rc.plot(y='O2[umol/kg]_ctd',x='O2[umol/kg]_winkler', legend=False,  \
 marker='o',mec='darkred', mfc='red', ms=7, mew=0.5, alpha=0.5, ls='', clip_on=False, zorder=100, ax=ax1)
    rc.plot(y='fit[umol/kg]',x='O2[umol/kg]_winkler', legend=False,  \
 linestyle='-',color='blue',clip_on=False, zorder=100, ax=ax1)  

    _dx1=15
    _dy1=0
# _dx2=10
    _dy2=-7
    _fcol='red'
    _tcol='red'

### 기울기, y절편, R-squred
# 폰트사이즈 12
    x_pos = rc[u'O2[umol/kg]_winkler'].median() +_dx1
    y_pos = rc[u'O2[umol/kg]_ctd'].median() + _dy1  
    ax1.text(x_pos, y_pos, 'slope, intercept, R$^2$', color='gray', fontsize=12)  
    ax1.text(x_pos, y_pos + _dy2,'%2.4f' % slope0 + ','+ '%2.4f' % intercept0 + ',' + '%2.4f' % rval0**2, color=_tcol, fontsize=12)  

### x축 이름, y축 이름
    ax1.set_xlabel("O2 [$\mu$mol/kg], Winkler", weight = 'semibold')
    ax1.set_ylabel("O2 [$\mu$mol/kg], SBE 43", weight = 'semibold') 
    plt.suptitle(cruise+st)   
    _dir = '/Users/jung-ok/work1/ARA13B/plot/winkler/'
    fname = 'linear regression'+'_winkler_ctd_'+cruise+st+'.png'
    plt.savefig(_dir+fname) 
    plt.show()



def plot_cmap_lr_winkler_ctd(cruise, st, slope0, intercept0, rval0, rc):
    fig = plt.figure(figsize=(7, 8))
    ax1= fig.add_axes([0.15, 0.1, 0.8, 0.7]) 

    minr,maxr = ymin, ymax
    clevs = np.linspace(minr,maxr,10)
    cs = ax1.scatter(y=rc['O2[umol/kg]_ctd'],x=rc['O2[umol/kg]_winkler'], c=rc['Depth_ctd'],
    vmin=minr, vmax=maxr, cmap='jet', edgecolor = 'k', s=60)
    rc.plot(y='fit[umol/kg]',x='O2[umol/kg]_winkler', legend=False,  \
 linestyle='-',color='blue',clip_on=False, zorder=100, ax=ax1)  

    fig.colorbar(cs, extend='max', ax=ax1, orientation = 'vertical', ticks = clevs)

    # _dx1=15
    # _dy1=0
#     _dx1=-50
#     _dy1=50
# # _dx2=10
#     _dy2=-5
    _fcol='red'
    _tcol='red'

## 기울기, y절편, R-squred
# 폰트사이즈 12
    x_pos = rc[u'O2[umol/kg]_winkler'].median() +float(_dx1)
    y_pos = rc[u'O2[umol/kg]_ctd'].median() + float(_dy1)  
    ax1.text(x_pos, y_pos, 'slope, intercept, R$^2$', color='gray', fontsize=12)  
    ax1.text(x_pos, y_pos + float(_dy2),'%2.4f' % slope0 + ','+ '%2.4f' % intercept0 + ',' + '%2.4f' % rval0**2, color=_tcol, fontsize=12)  

### x축 이름, y축 이름
    ax1.set_xlabel("O2 [$\mu$mol/kg], Winkler", weight = 'semibold')
    ax1.set_ylabel("O2 [$\mu$mol/kg], SBE 43", weight = 'semibold') 
    plt.suptitle(cruise+st)   
    _dir = '/Users/jung-ok/work1/ARA13B/plot/winkler/'
    fname = 'cmap_linear regression'+'_winkler_ctd_'+cruise+st+'.png'
    plt.savefig(_dir+fname) 
    plt.show()

### cruise name 
# example: ARA13B
print("cruise: cruise name")
cruise = input("cruise = ")

### Winkler 
# 정점 01번
# 정점 17번
# 정점 22번
# 정점 23번
# 정점 34번
# 정점 42번
# 정점 49번
# 정점 55번

w_folder='/Users/jung-ok/work1/ARA13B/raw_data/Winkler/new/'
winkler_files =sorted(glob(w_folder+'*.csv'))

c_folder='/Users/jung-ok/work1/ARA13B/raw_data/CTD/bottle_summary/new/'
ctd_files =sorted(glob(c_folder+'*.csv'))

# ###
# # print("File Name")
i = input("i = ")
print(winkler_files[int(i)])
# i=0 ; st='023'
# i=1 ; st='034'
# i=2 ; st='066'
# i=3 ; st='082'
# i=4 ; st='84'
# i=5 ; st='85'

print("Station Number")
st = input("st = ")

print("Cast Number")
cast = input("cast = ")

fname = cruise+st+'CTD'+cast+'.csv'
print(fname)

dw = pd.read_csv(winkler_files[int(i)], index_col=None)
dc= pd.read_csv(c_folder+fname, index_col=None)

dc.rename(columns = {'Bottle':'Niskin_#','Depth [salt water, m]':'Depth', 'Oxygen, SBE 43 [umol/kg]':'O2[umol/kg]'}, inplace=True)

print("Depth, Max")
print(dw['Depth'].max())

ymin = 0
# ymax = input("ymax = ")
ymax = int(input("ymax = "))

## ARA13B St.023
## Depth [m] min 0,  max 210
# ymax=212 ; ymin=0
## ARA13B St.034
## Depth [m] min 0,  max 1009.0
# ymax=3500 ; ymin=0
## ARA13B St.84
## Depth [m] min 0,  max 2088
# ymax=2100 ; ymin=0

if st=='34':
    dc['Niskin_#'][0]=1
    dc['Niskin_#'][1]=2
    dc['Niskin_#'][2]=3
    dc['Niskin_#'][3]=4
    dc['Niskin_#'][4]=5
    dc['Niskin_#'][5]=6
    dc['Niskin_#'][6]=7
    dc['Niskin_#'][7]=8
    dc['Niskin_#'][8]=9
    dc['Niskin_#'][9]=10
    dc['Niskin_#'][10]=11
    dc['Niskin_#'][11]=12
    dc['Niskin_#'][12]=13
    dc['Niskin_#'][13]=14
    dc['Niskin_#'][14]=15
    dc['Niskin_#'][15]=16
    dc['Niskin_#'][16]=17
    dc['Niskin_#'][17]=18
    dc['Niskin_#'][18]=19
    dc['Niskin_#'][19]=20
    dc['Niskin_#'][20]=21
    dc['Niskin_#'][21]=22
    dc['Niskin_#'][22]=23
    dc['Niskin_#'][23]=24
elif st=='66':
    dc['Niskin_#'][0]=1
    dc['Niskin_#'][1]=2
    dc['Niskin_#'][2]=3
    dc['Niskin_#'][3]=4
    dc['Niskin_#'][4]=5
    dc['Niskin_#'][5]=6
    dc['Niskin_#'][6]=7
    dc['Niskin_#'][7]=8
    dc['Niskin_#'][8]=9
    dc['Niskin_#'][9]=10
    dc['Niskin_#'][10]=11
    dc['Niskin_#'][11]=12
    dc['Niskin_#'][12]=13
    dc['Niskin_#'][13]=14
    dc['Niskin_#'][14]=15
    dc['Niskin_#'][15]=16
    dc['Niskin_#'][16]=17
    dc['Niskin_#'][17]=18
    dc['Niskin_#'][18]=19
    dc['Niskin_#'][19]=20
    dc['Niskin_#'][20]=21
    dc['Niskin_#'][21]=22
    dc['Niskin_#'][22]=23
    dc['Niskin_#'][23]=24        
else:
    dc['Niskin_#'][0]=1
    dc['Niskin_#'][2]=2
    dc['Niskin_#'][3]=3
    dc['Niskin_#'][4]=4
    dc['Niskin_#'][5]=5
    dc['Niskin_#'][6]=6
    dc['Niskin_#'][7]=7
    dc['Niskin_#'][8]=8
    dc['Niskin_#'][9]=9
    dc['Niskin_#'][10]=10
    dc['Niskin_#'][11]=11
    dc['Niskin_#'][12]=12
    dc['Niskin_#'][13]=13
    dc['Niskin_#'][14]=14
    dc['Niskin_#'][15]=15
    dc['Niskin_#'][16]=16
    dc['Niskin_#'][17]=17
    dc['Niskin_#'][18]=18
    dc['Niskin_#'][19]=19
    dc['Niskin_#'][20]=20
    dc['Niskin_#'][21]=21
    dc['Niskin_#'][22]=22
    dc['Niskin_#'][1]=23
    dc['Niskin_#'][23]=24



if st=='23':
    dw['O2[umol/kg]'][0]=np.nan
if st=='66':
    dw['O2[umol/kg]'][2]=np.nan    
if st=='82':
    dw['O2[umol/kg]'][dw.index==16]=np.nan 
    dw['Niskin_#'][dw.index==16]=14
    # dw['Niskin_#'][dw.index==0]=2
    dw['Bottle_#'][dw.index==16]=18
if st=='84':
    dw['Niskin_#'][4:6]=6    
else:
    pass # do nothing


# St. 82
# Niskin_# 1인 행을 제거
if st=='82':
    dw['O2[umol/kg]'][dw['Niskin_#']==1]=np.nan
    dw=dw.drop([0,1,2])


plot_depth_profile_winkler_ctd(st, dw, dc, ymin, ymax)



_cols = ['Niskin_#', 'Depth',  'O2[umol/kg]']
nw=dw[_cols][0:].groupby(['Niskin_#']).mean().reset_index()
nc=dc[_cols]

wc = pd.merge(left=nw, right=nc, left_on='Niskin_#', right_on='Niskin_#', how='inner')
wc.rename(columns = {'Depth_x':'Depth_winkler', 'O2[umol/kg]_x':'O2[umol/kg]_winkler', 'Depth_y':'Depth_ctd', 'O2[umol/kg]_y':'O2[umol/kg]_ctd'}, inplace=True)

wc['DO2[umol/kg]']=wc['O2[umol/kg]_ctd']-wc['O2[umol/kg]_winkler']

# scatter plot, 수평축: winkler 용존산소농도, 수직축: ctd 용존산소농도
wc.plot(y='O2[umol/kg]_ctd',x='O2[umol/kg]_winkler', legend=False,  \
 marker='o',mec='darkred', mfc='red', ms=7, mew=0.5, alpha=0.5, ls='', clip_on=False, zorder=100)
plt.show()

_dir = '/Users/jung-ok/work1/ARA13B/processed/Winkler/'
fname = 'check'+'_winkler_ctd_'+cruise+st+'.csv'
wc.to_csv(_dir+fname, index=False, na_rep=np.nan, float_format='%g')

rc = wc.copy()
rc = wc.sort_values('O2[umol/kg]_winkler')

### 회귀선
xval=rc[u'O2[umol/kg]_winkler']
yval=rc[u'O2[umol/kg]_ctd']
slope0, intercept0, rval0, pval0, std_err0 = linregress(xval,yval)

rc['fit[umol/kg]']=float(slope0)*rc[u'O2[umol/kg]_winkler']+float(intercept0)

plot_lr_winkler_ctd(cruise, st, slope0, intercept0, rval0, rc)

# x_pos = rc[u'O2[umol/kg]_winkler'].median() +float(_dx1)
# y_pos = rc[u'O2[umol/kg]_ctd'].median() + float(_dy1)  
# ax1.text(x_pos, y_pos, 'slope, intercept, R$^2$', color='gray', fontsize=12)  
# ax1.text(x_pos, y_pos + float(_dy2),'%2.4f' % slope0 + ','+ '%2.4f' % intercept0 + ',' + '%2.4f' % rval0**2, color=_tcol, fontsize=12)  

print(rc[u'O2[umol/kg]_winkler'].median(), rc[u'O2[umol/kg]_ctd'].median())

# _dy2 = -5

# st 23
# _dx1 = -50-20
# _dy1 = 50+15

# st 34
# _dx1 = -50+10
# _dy1 = 50+40

# st 66
# _dx1 = -50
# _dy1 = 120

# st 82
# _dx1 = -50+20
# _dy1 = 50+35

# st 84
# _dx1 = -50+10
# _dy1 = 50+30

# st 85
# _dx1 = -50-10
# _dy1 = 50


print("_dx1")
_dx1 = input("_dx1 = ")
print("_dy1")
_dy1 = input("_dy1 = ")
print("_dy2")
_dy2 = input("_dy2 = ")

plot_cmap_lr_winkler_ctd(cruise, st, slope0, intercept0, rval0, rc)


### 수정하시오
# plt.barh(range(len(rc['Depth_winkler'])),rc['DO2[umol/kg]'], align='center')
# plt.yticks(range(len(rc['Depth_winkler'])), rc['Depth_winkler']) 
# _dir = '/Users/jung-ok/work1/ARA13B/plot/winkler/'
# fname = 'barh_depth_diff'+'_winkler_ctd_'+cruise+st+'.png'
# plt.savefig(_dir+fname) 
# plt.show()

# plt.barh(range(len(rc['O2[umol/kg]_winkler'])),rc['DO2[umol/kg]'], align='center')
# plt.yticks(range(len(rc['O2[umol/kg]_winkler'])), rc['O2[umol/kg]_winkler']) 
# _dir = '/Users/jung-ok/work1/ARA13B/plot/winkler/'
# fname = 'barh_O2_conc_diff'+'_winkler_ctd_'+cruise+st+'.png'
# plt.savefig(_dir+fname) 
# plt.show()
