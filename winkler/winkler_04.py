import re
import pandas as pd
import matplotlib.pyplot as plt1
import numpy as np
from glob import glob
import datetime
import string
from scipy.stats import linregress


# cruise=input('cruise= ')
cruise='ARA13B'


# input file : 
# Winkler03.py 실행 후 출력파일 
do_files =sorted(glob('/Users/jung-ok/work1/'+cruise+'/processed/Winkler/dissolved*.csv'))

print("i: index of file list")
i = int(input("i = "))

# cruise=do_files[i].split('/')[-1].split('.')[0][-8:-2]
st=do_files[i].split('/')[-1].split('.')[0][-2:]

do_table= pd.read_csv(do_files[i], index_col=None)

##### flag #####
# :0
# n>30 : 1
# outlier: 3
# no value, NaN: 5

### 데이터 프레임 구분 : 'flag' 열 추가
# fo       : outlier 포함
do_table['flag']=0
fo=do_table[do_table['flag']==0]

# if i==0:      
#    fo['flag'][16]=3
#    fo['flag'][17]=3  
# elif i==3:      
#    fo['flag'][8]=3    
# elif i==4:      
#    fo['flag'][20]=3
#    fo['flag'][21]=3 
    
# co=fo[['Station', 'Depth [salt water, m]', 'Niskin_#', 'Oxygen, Winkler [umol/kg]', u'Oxygen, SBE 43 [umol/kg]', 'flag']]
co=fo[['Station', 'Depth [salt water, m]', 'Niskin_#', 'Oxygen, Winkler [umol/kg]', u'Oxygen, SBE 43 [umol/kg]']]

# fname = '/Users/jung-ok/work1/'+cruise+'/processed/Winkler/DO_Winkler_CTD_'+cruise+st+'_flag'+'.csv'
fname = '/Users/jung-ok/work1/'+cruise+'/processed/Winkler/DO_Winkler_CTD_'+cruise+st+'.csv'

co.sort_values(by=['Depth [salt water, m]'], ascending=True).to_csv(fname, index=False, na_rep=np.nan, float_format='%g')

print("Done")

# # merge
# path ='/Users/jung-ok/work1/ANA11/processed/winkler/' # use your path
# files = sorted(glob(path + "/*.csv"))
# frame = pd.DataFrame()
# list_ = []
# for file_ in files:
#     df = pd.read_csv(file_,index_col=None, header=0)
#     list_.append(df)
# frame = pd.concat(list_)
# folder='/Users/jung-ok/work1/ANA11/processed/winkler/'
# fname='dissolved_oxygen_Winkler_CTD_flag_station'+'_04_09_25'+'.csv'
# frame.to_csv(folder+fname, index=False, na_rep=np.nan, float_format='%5.3f')

