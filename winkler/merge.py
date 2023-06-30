import datetime
from glob import glob

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Image
from matplotlib import dates

import xlrd

### winkler04.py
# (Winkler vs. CTD) 경향성에서 벗어난 데이터를 제외, flag > 1
# 파일 새로 생성


# input file : 
#winkler04.py 실행 후 출력파일 
files =sorted(glob('/Users/jung-ok/work1/ARA13B/processed/Winkler/DO*.csv'))

# for b, fname in enumerate(files):
#     print(b, fname)

##### ARA13B01
i=0
a01 = pd.read_csv(files[i], parse_dates=True, index_col=None) 
##### ARA13B17
i=1
a17 = pd.read_csv(files[i], parse_dates=True, index_col=None) 
##### ARA13B22
i=2
a22 = pd.read_csv(files[i], parse_dates=True, index_col=None) 
##### ARA13B23 
i=3
a23 = pd.read_csv(files[i], parse_dates=True, index_col=None) 
##### ARA13B34 
i=4
a34 = pd.read_csv(files[i], parse_dates=True, index_col=None) 
##### ARA13B42 
i=5
a42 = pd.read_csv(files[i], parse_dates=True, index_col=None) 
##### ARA13B49 
i=6
a49 = pd.read_csv(files[i], parse_dates=True, index_col=None) 
##### ARA13B55
i=7
a55 = pd.read_csv(files[i], parse_dates=True, index_col=None) 


out_file='/Users/jung-ok/work1/ARA13B/processed/winkler/DO_winkler_CTD_ARA13B.xlsx'

# ARA13B
with pd.ExcelWriter(out_file) as writer:
    a01.to_excel(writer, sheet_name='ARA13B01', index=False)
    a17.to_excel(writer, sheet_name='ARA13B17', index=False)
    a22.to_excel(writer, sheet_name='ARA13B22', index=False)
    a23.to_excel(writer, sheet_name='ARA13B23', index=False)
    a34.to_excel(writer, sheet_name='ARA13B34', index=False)
    a42.to_excel(writer, sheet_name='ARA13B42', index=False)
    a49.to_excel(writer, sheet_name='ARA13B49', index=False)
    a55.to_excel(writer, sheet_name='ARA13B55', index=False)    

    writer.save() 

print ('Done')

