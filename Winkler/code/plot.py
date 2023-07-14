do_table['winkler-corrected']=   do_table['O2[umol/kg]']-do_table['O2[umol/kg], corrected']
    
do_table['winkler-SBE']=   do_table['O2[umol/kg]']-do_table['Oxygen, SBE 43 [umol/kg]']      
    
do_table['corrected-SBE']=   do_table['O2[umol/kg], corrected'] - do_table[u'Oxygen, SBE 43 [umol/kg]']
    


do_table[['Depth [salt water, m]','winkler-corrected','winkler-SBE','corrected-SBE']]




# station 25
# xmin=190;xmax=400
xw=350
xc=350
yw= 280
yc=200



# station 04
# xmin=190;xmax=400
xw=350
xc=350
yw= 280
yc=200



# station 09
# xmin=190;xmax=400
xw=225
xc=225
yw= 400
yc=500



import matplotlib 
matplotlib.rcParams.update({'font.size': 10, 'font.weight':'bold'})

# fig, ax1 = plt.subplots(figsize=(9, 9))

fig = plt.figure(figsize=(6, 9))
ax1= fig.add_axes([0.15, 0.1, 0.8, 0.7]) 

# matplotlib.rcParams.update({u'xtick.color': u'green'})
# # restore
# matplotlib.rcParams.update({u'xtick.color': u'k'})
# ax1.spines['bottom'].set_color('green')



db.plot(y=u'Depth [salt water, m]',x=u'Oxygen, SBE 43 [umol/kg]',legend=False, ax=ax1,         marker='o',markeredgecolor='darkgreen', markerfacecolor='green',markersize=7,mew=0.5, alpha=0.2,        linestyle='-',color='g',clip_on=False, zorder=100);
do_table.plot(y=u'Depth [salt water, m]',x='O2[umol/kg], corrected',legend=False,  ax=ax1,         marker='o',markeredgecolor='darkolivegreen', markerfacecolor='olive', markersize=7, mew=1,        linestyle='', clip_on=False, zorder=100);

#station 09
do_table[do_table['Depth [salt water, m]']==150].plot(y=u'Depth [salt water, m]',x=u'O2[umol/kg], corrected',legend=False, 
       marker='o',markeredgecolor='darkred', markerfacecolor='red',markersize=7,mew=1, alpha=0.5,\
       linestyle='',color='red', clip_on=False, zorder=100, ax=ax1);

# #station 04
# do_table[do_table['Depth [salt water, m]']==160].plot(y=u'Depth [salt water, m]',x=u'O2[umol/kg], corrected',legend=False, 
#        marker='o',markeredgecolor='darkred', markerfacecolor='red',markersize=7,mew=1, alpha=0.5,\
#        linestyle='',color='red', clip_on=False, zorder=100, ax=ax1);


# ymax=580;ymin=0
ax1.set_ylim(ymax,ymin)
# xmin=230;xmax=430
ax1.set_xlim(xmin,xmax)
ax1.set_xlabel('O2 [umol/kg]', fontsize=10, weight = 'semibold', color='black')#color='green'
ax1.set_ylabel('Depth [salt water, m] [m]', fontsize=10, weight = 'semibold')
# ax.set_title('Dissolved Oxygen', fontsize=20)  
ax1.set_title('Station '+str(st)+',  ARA10B')
# ax1.text(235, 700,'Station 09', color='k')
# ax1.text(xw, 350,'Winkler', color='olive')     
# ax1.text(xw, 300,'SBE 43', color='g')
ax1.text(xw, yw,'Winkler', color='olive')     
ax1.text(xw, yc,'SBE 43', color='g')


folder='/work1/ARA10B/plot/winkler/'
fname='Depth [salt water, m]_profile_winkler_ctd_st'+str(st)+'.png'
plt.savefig(folder+fname) 



do_table.columns




## station 25, bottle 05, n>30

do_table[u'Oxygen, SBE 43 [umol/kg]'][do_table['Bottle_#']==5]=np.nan

   
do_table[['Depth [salt water, m]', 'O2[uM]', 'O2[umol/kg]', 'Bottle_#', 'End_Point', u'Oxygen, SBE 43 [umol/kg]']][do_table['Bottle_#']==5]   



## station 04,  n>30

# bottle=[25, 81, 28, 55, 52, 24, 22, 2]
bottle=[2]

for i in np.arange(len(bottle)):
    b=bottle[i]
#     print i, b
#     dw['O2[uM]'][dw['Bottle_#']==b]=np.nan
#     dw['O2[umol/kg]'][dw['Bottle_#']==b]=np.nan
#     dw['End_Point'][dw['Bottle_#']==b]=np.nan
    
    do_table[u'Oxygen, SBE 43 [umol/kg]'][do_table['Bottle_#']==b]=np.nan




## station 25
do_table['flag']=0
## n>30, flag=1 but temporarily flag=5,  after getting the calculated value it must be modified
do_table[u'flag'][do_table['Bottle_#']==5]=5
fo=do_table[do_table['flag']==0]

xval=fo[u'O2[umol/kg], corrected'].dropna()
yval=fo[u'Oxygen, SBE 43 [umol/kg]'].dropna()
slope, intercept, rval, pval, std_err = linregress(xval,yval)

# fo['fit[umol/kg]'] = np.nan
fo['fit[umol/kg]']=float(slope0)*fo[u'O2[umol/kg], corrected']+float(intercept0)




## station 09
do_table['flag']=0
# do_table[u'flag'][do_table['Depth [salt water, m]']==150]=3
fo=do_table[do_table['flag']==0]

xval=fo[u'O2[umol/kg], corrected'].dropna()
yval=fo[u'Oxygen, SBE 43 [umol/kg]'].dropna()
slope0, intercept0, rval0, pval0, std_err0 = linregress(xval,yval)

# fo['fit[umol/kg]'] = np.nan
fo['fit[umol/kg]']=float(slope0)*fo[u'O2[umol/kg], corrected']+float(intercept0)



## station 09
fo['flag'][fo['Depth [salt water, m]']==150]=3
go=fo[fo['flag']<=1]


xval=go[u'O2[umol/kg], corrected'].dropna()
yval=go[u'Oxygen, SBE 43 [umol/kg]'].dropna()
slope, intercept, rval, pval, std_err = linregress(xval,yval)

# fo['fit[umol/kg]'] = np.nan
go['fit[umol/kg]']=float(slope)*go[u'O2[umol/kg], corrected']+float(intercept)




## station 04,  n>30

do_table['flag']=0

# bottle=[25, 81, 28, 55, 52, 24, 22, 2]
bottle=[2]

for i in np.arange(len(bottle)):
    b=bottle[i]
    do_table[u'flag'][do_table['Bottle_#']==b]=5
    
    
bottle=[25, 81, 28, 55, 52, 24, 22]
# bottle=[2]

for i in np.arange(len(bottle)):
    b=bottle[i]
    do_table[u'flag'][do_table['Bottle_#']==b]=1


fo=do_table[(do_table['flag']<=1)]
# fo


xval=fo[u'O2[umol/kg], corrected'].dropna()
yval=fo[u'Oxygen, SBE 43 [umol/kg]'].dropna()
slope, intercept, rval, pval, std_err = linregress(xval,yval)

# fo['fit[umol/kg]'] = np.nan
fo['fit[umol/kg]']=float(slope)*fo[u'O2[umol/kg], corrected']+float(intercept)



## station 04
fo['flag'][fo['Depth [salt water, m]']==160]=3
go=fo[fo['flag']<=1]


xval=go[u'O2[umol/kg], corrected'].dropna()
yval=go[u'Oxygen, SBE 43 [umol/kg]'].dropna()
slope, intercept, rval, pval, std_err = linregress(xval,yval)

# fo['fit[umol/kg]'] = np.nan
go['fit[umol/kg]']=float(slope)*go[u'O2[umol/kg], corrected']+float(intercept)




go[[u'O2[umol/kg], corrected']].sort_values(u'O2[umol/kg], corrected')




### station 25
get_ipython().run_line_magic('matplotlib', '')
fig = plt.subplots(figsize=(8, 8))

ax1=plt.subplot(1,1,1);
ax1.spines['bottom'].set_color('k')

for label in ax1.get_xticklabels():
    label.set_color('k')    

fo.sort_values(u'O2[umol/kg], corrected').plot(       y=u'Oxygen, SBE 43 [umol/kg]',x=u'O2[umol/kg], corrected',
       marker='o',markeredgecolor='darkgreen', markerfacecolor='green',markersize=7,mew=0.5, alpha=0.5,\
       linestyle='--',color='green',clip_on=False, zorder=100, ax=ax1, legend=False);

fo.sort_values(u'O2[umol/kg], corrected').plot(y=u'fit[umol/kg]',x=u'O2[umol/kg], corrected',legend=False, 
#        marker='o',markeredgecolor='darkblue', markerfacecolor='blue',markersize=7,mew=0.5, alpha=0.3,\
       linestyle='-',color='blue',clip_on=False, zorder=100, ax=ax1);

ax1.set_xlabel("O2 [$\mu$mol/kg], Winkler", weight = 'semibold')
ax1.set_ylabel("O2 [$\mu$mol/kg], SBE 43", weight = 'semibold')

ax1.text(270, 370,'Station 25', color='k')

ax1.text(270, 360,         '( slope, intercept, R$^2$ )', color='gray')

# ax1.text(235, 370,'( '+ '%2.4f' % slope0 + ','+ '%2.4f' % intercept0 + ',' + '%2.4f' % rval0**2 + ' )', \   
#          color='red')     
ax1.text(270, 355,'( '+ '%2.4f' % slope + ','+ '%2.4f' % intercept + ',' + '%2.4f' % rval**2 + ' )',          color='blue')   
# ax1.text(235, 850,'Winkler', color='olive')  
file_name = '/work1/ARA10B/plot/winkler/calibration_winkler_ctd_st25_corrected.png'
plt.savefig(file_name)





### station 09
get_ipython().run_line_magic('matplotlib', '')
fig = plt.subplots(figsize=(8, 8))

ax1=plt.subplot(1,1,1);
ax1.spines['bottom'].set_color('k')

for label in ax1.get_xticklabels():
    label.set_color('k')    

fo.sort_values(u'O2[umol/kg], corrected').plot(       y=u'Oxygen, SBE 43 [umol/kg]',x=u'O2[umol/kg], corrected',
       marker='o',markeredgecolor='darkgreen', markerfacecolor='green',markersize=7,mew=0.5, alpha=0.5,\
       linestyle='--',color='green',clip_on=False, zorder=100, ax=ax1, legend=False);

fo.sort_values(u'O2[umol/kg], corrected').plot(y=u'fit[umol/kg]',x=u'O2[umol/kg], corrected',legend=False, 
#        marker='o',markeredgecolor='darkblue', markerfacecolor='blue',markersize=7,mew=0.5, alpha=0.3,\
       linestyle='-',color='red',clip_on=False, zorder=100, ax=ax1);

fo[fo['Depth [salt water, m]']==150].plot(y=u'Oxygen, SBE 43 [umol/kg]',x=u'O2[umol/kg], corrected',legend=False, 
       marker='o',markeredgecolor='darkred', markerfacecolor='red',markersize=7,mew=0.5, alpha=0.5,\
       linestyle='',color='red', clip_on=False, zorder=100, ax=ax1);

go.sort_values(u'O2[umol/kg], corrected').plot(y=u'fit[umol/kg]',x=u'O2[umol/kg], corrected',legend=False, 
#        marker='o',markeredgecolor='darkblue', markerfacecolor='blue',markersize=7,mew=0.5, alpha=0.3,\
       linestyle='-',color='blue',clip_on=False, zorder=100, ax=ax1);

ax1.set_xlabel("O2 [$\mu$mol/kg], Winkler", weight = 'semibold')
ax1.set_ylabel("O2 [$\mu$mol/kg], SBE 43", weight = 'semibold')

ax1.text(270, 370,'Station 09', color='k')

ax1.text(270, 360,         '( slope, intercept, R$^2$ )', color='gray')

# ax1.text(235, 370,'( '+ '%2.4f' % slope0 + ','+ '%2.4f' % intercept0 + ',' + '%2.4f' % rval0**2 + ' )', \   
#          color='red')     
ax1.text(270, 355,'( '+ '%2.4f' % slope0 + ','+ '%2.4f' % intercept0 + ',' + '%2.4f' % rval0**2 + ' )',          color='red')   
ax1.text(270, 350,'( '+ '%2.4f' % slope + ','+ '%2.4f' % intercept + ',' + '%2.4f' % rval**2 + ' )',          color='blue')
# ax1.text(235, 850,'Winkler', color='olive')  
file_name = '/work1/ARA10B/plot/winkler/calibration_winkler_ctd_st09_corrected.png'
plt.savefig(file_name)



# station 04
get_ipython().run_line_magic('matplotlib', '')
fig = plt.subplots(figsize=(8, 8))

ax1=plt.subplot(1,1,1);
ax1.spines['bottom'].set_color('k')

for label in ax1.get_xticklabels():
    label.set_color('k')    

fo.sort_values(u'O2[umol/kg], corrected').plot(       y=u'Oxygen, SBE 43 [umol/kg]',x=u'O2[umol/kg], corrected',
       marker='o',markeredgecolor='darkgreen', markerfacecolor='green',markersize=7,mew=0.5, alpha=0.5,\
       linestyle='--',color='green',clip_on=False, zorder=100, ax=ax1, legend=False);

fo.sort_values(u'O2[umol/kg], corrected').plot(y=u'fit[umol/kg]',x=u'O2[umol/kg], corrected',legend=False, 
#        marker='o',markeredgecolor='darkblue', markerfacecolor='blue',markersize=7,mew=0.5, alpha=0.3,\
       linestyle='-',color='red',clip_on=False, zorder=100, ax=ax1);

fo[fo['Depth [salt water, m]']==160].plot(y=u'Oxygen, SBE 43 [umol/kg]',x=u'O2[umol/kg], corrected',legend=False, 
       marker='o',markeredgecolor='darkred', markerfacecolor='red',markersize=7,mew=0.5, alpha=0.5,\
       linestyle='',color='red', clip_on=False, zorder=100, ax=ax1);

go.sort_values(u'O2[umol/kg], corrected').plot(y=u'fit[umol/kg]',x=u'O2[umol/kg], corrected',legend=False, 
#        marker='o',markeredgecolor='darkblue', markerfacecolor='blue',markersize=7,mew=0.5, alpha=0.3,\
       linestyle='-',color='blue',clip_on=False, zorder=100, ax=ax1);

ax1.set_xlabel("O2 [$\mu$mol/kg], Winkler", weight = 'semibold')
ax1.set_ylabel("O2 [$\mu$mol/kg], SBE 43", weight = 'semibold')

ax1.text(270, 370,'Station 04', color='k')

ax1.text(270, 360,         '( slope, intercept, R$^2$ )', color='gray')

# ax1.text(235, 370,'( '+ '%2.4f' % slope0 + ','+ '%2.4f' % intercept0 + ',' + '%2.4f' % rval0**2 + ' )', \   
#          color='red')     
ax1.text(270, 355,'( '+ '%2.4f' % slope0 + ','+ '%2.4f' % intercept0 + ',' + '%2.4f' % rval0**2 + ' )',          color='red')   
ax1.text(270, 350,'( '+ '%2.4f' % slope + ','+ '%2.4f' % intercept + ',' + '%2.4f' % rval**2 + ' )',          color='blue')
# ax1.text(235, 850,'Winkler', color='olive')  
file_name = '/work1/ARA10B/plot/winkler/calibration_winkler_ctd_st04_corrected.png'
plt.savefig(file_name)




### station 04
bottle=[2]

for i in np.arange(len(bottle)):
    b=bottle[i]
    do_table[u'flag'][do_table['Bottle_#']==b]=5
    
    
bottle=[25, 81, 28, 55, 52, 24, 22]
# bottle=[2]

for i in np.arange(len(bottle)):
    b=bottle[i]
    do_table[u'flag'][do_table['Bottle_#']==b]=1
    
do_table['flag'][do_table['Depth [salt water, m]']==160]=3    
    
co=do_table[['Station', 'Depth [salt water, m]', 'O2[umol/kg], corrected', u'Oxygen, SBE 43 [umol/kg]', 'flag']]
co.columns=['Station', 'Depth [salt water, m] [m]', 'O2 [umol/kg], Winkler', u'Oxygen, SBE 43 [umol/kg]', 'flag']

folder='/work1/ARA10B/processed/winkler/'
fname='dissolved_oxygen_Winkler_CTD_station'+str(st)+'.csv'
co.to_csv(folder+fname, index=False, na_rep=np.nan, float_format='%5.3f')




### station 09
# bottle=[2]

# for i in np.arange(len(bottle)):
#     b=bottle[i]
#     do_table[u'flag'][do_table['Bottle_#']==b]=5
    
    
# bottle=[25, 81, 28, 55, 52, 24, 22]
# # bottle=[2]

# for i in np.arange(len(bottle)):
#     b=bottle[i]
#     do_table[u'flag'][do_table['Bottle_#']==b]=1
    
do_table['flag'][do_table['Depth [salt water, m]']==150]=3    
    
co=do_table[['Station', 'Depth [salt water, m]', 'O2[umol/kg], corrected', u'Oxygen, SBE 43 [umol/kg]', 'flag']]
co.columns=['Station', 'Depth [salt water, m] [m]', 'O2 [umol/kg], Winkler', u'Oxygen, SBE 43 [umol/kg]', 'flag']

folder='/work1/ARA10B/processed/winkler/'
fname='dissolved_oxygen_Winkler_CTD_station'+str(st)+'.csv'
co.to_csv(folder+fname, index=False, na_rep=np.nan, float_format='%5.3f')




### station 25
## n>30, flag=1 but temporarily flag=5,  after getting the calculated value it must be modified
bottle=[5]

for i in np.arange(len(bottle)):
    b=bottle[i]
    do_table[u'flag'][do_table['Bottle_#']==b]=5
    
    
# bottle=[25, 81, 28, 55, 52, 24, 22]
# # bottle=[2]

# for i in np.arange(len(bottle)):
#     b=bottle[i]
#     do_table[u'flag'][do_table['Bottle_#']==b]=1
    
# do_table['flag'][do_table['Depth [salt water, m]']==150]=3    
    
co=do_table[['Station', 'Depth [salt water, m]', 'O2[umol/kg], corrected', u'Oxygen, SBE 43 [umol/kg]', 'flag']]
co.columns=['Station', 'Depth [salt water, m] [m]', 'O2 [umol/kg], Winkler', u'Oxygen, SBE 43 [umol/kg]', 'flag']

folder='/work1/ARA10B/processed/winkler/'
fname='dissolved_oxygen_Winkler_CTD_station'+str(st)+'.csv'
co.to_csv(folder+fname, index=False, na_rep=np.nan, float_format='%5.3f')


# # merge

# In[121]:


path ='/work1/ARA10B/processed/winkler/' # use your path
allFiles = sorted(glob(path + "/*.csv"))
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
frame = pd.concat(list_)




frame.head()




frame.tail()




frame.columns




## station 04, 09, 25
fo=frame
go=fo[fo['flag']<=1]


xval=go[u'O2 [umol/kg], Winkler'].dropna()
yval=go[u'Oxygen, SBE 43 [umol/kg]'].dropna()
slope, intercept, rval, pval, std_err = linregress(xval,yval)

# fo['fit[umol/kg]'] = np.nan
go['fit[umol/kg]']=float(slope)*go[u'O2 [umol/kg], Winkler']+float(intercept)




### station 04,09,25
get_ipython().run_line_magic('matplotlib', '')
fig = plt.subplots(figsize=(8, 8))

ax1=plt.subplot(1,1,1);
ax1.spines['bottom'].set_color('k')

for label in ax1.get_xticklabels():
    label.set_color('k')    

go.sort_values(u'O2 [umol/kg], Winkler').plot(       y=u'Oxygen, SBE 43 [umol/kg]',x= u'O2 [umol/kg], Winkler',
       marker='o',markeredgecolor='darkgreen', markerfacecolor='green',markersize=7,mew=0.5, alpha=0.5,\
       linestyle='--',color='green',clip_on=False, zorder=100, ax=ax1, legend=False);

# fo.sort_values(u'O2 [umol/kg], Winkler').plot(y=u'fit[umol/kg]',x= u'O2 [umol/kg], Winkler',legend=False, 
# #        marker='o',markeredgecolor='darkblue', markerfacecolor='blue',markersize=7,mew=0.5, alpha=0.3,\
#        linestyle='-',color='red',clip_on=False, zorder=100, ax=ax1);

# fo[fo['Depth [salt water, m]']==150].plot(y=u'Oxygen, SBE 43 [umol/kg]',x=u'O2 [umol/kg], Winkler',legend=False, 
#        marker='o',markeredgecolor='darkred', markerfacecolor='red',markersize=7,mew=0.5, alpha=0.5,\
#        linestyle='',color='red', clip_on=False, zorder=100, ax=ax1);

go.sort_values( u'O2 [umol/kg], Winkler').plot(y=u'fit[umol/kg]',x= u'O2 [umol/kg], Winkler',legend=False, 
#        marker='o',markeredgecolor='darkblue', markerfacecolor='blue',markersize=7,mew=0.5, alpha=0.3,\
       linestyle='-',color='blue',clip_on=False, zorder=100, ax=ax1);

ax1.set_xlabel("O2 [$\mu$mol/kg], Winkler", weight = 'semibold')
ax1.set_ylabel("O2 [$\mu$mol/kg], SBE 43", weight = 'semibold')

# ax1.text(270, 370,'Station 09', color='k')

ax1.text(270, 360,         '( slope, intercept, R$^2$ )', color='gray')

# ax1.text(235, 370,'( '+ '%2.4f' % slope0 + ','+ '%2.4f' % intercept0 + ',' + '%2.4f' % rval0**2 + ' )', \   
#          color='red')     
# ax1.text(270, 355,'( '+ '%2.4f' % slope0 + ','+ '%2.4f' % intercept0 + ',' + '%2.4f' % rval0**2 + ' )', \
#          color='red')   
ax1.text(270, 350,'( '+ '%2.4f' % slope + ','+ '%2.4f' % intercept + ',' + '%2.4f' % rval**2 + ' )',          color='blue')
# ax1.text(235, 850,'Winkler', color='olive')  
file_name = '/work1/ARA10B/plot/winkler/calibration_winkler_ctd_station_04_09_25.png'
plt.savefig(file_name)




folder='/work1/ARA10B/processed/winkler/'
fname='dissolved_oxygen_Winkler_CTD_station'+'_04_09_25'+'.csv'
frame.to_csv(folder+fname, index=False, na_rep=np.nan, float_format='%5.3f')



pd.read_csv(folder+fname)



