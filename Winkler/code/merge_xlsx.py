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
files =sorted(glob('/Users/jung-ok/work1/ANA13B/processed/Winkler/LAB/DO*.csv'))

# for b, fname in enumerate(files):
#     print(b, fname)

##### ANA13B001
i=0
a001 = pd.read_csv(files[i], parse_dates=True, index_col=None) 
##### ANA13B041
i=1
a041 = pd.read_csv(files[i], parse_dates=True, index_col=None) 
##### ANA13B050
i=2
a050 = pd.read_csv(files[i], parse_dates=True, index_col=None) 
##### ANA13B061
i=3
a061 = pd.read_csv(files[i], parse_dates=True, index_col=None) 
##### ANA13B080
i=4
a080 = pd.read_csv(files[i], parse_dates=True, index_col=None) 
##### ANA13B089
i=5
a089 = pd.read_csv(files[i], parse_dates=True, index_col=None) 
##### ANA13B103
i=6
a103 = pd.read_csv(files[i], parse_dates=True, index_col=None) 



out_file='/Users/jung-ok/work1/ANA13B/processed/winkler/LAB/DO_winkler_CTD_ANA13B.xlsx'

# ARA13B
with pd.ExcelWriter(out_file) as writer:
    a001.to_excel(writer, sheet_name='ANA13B001', index=False)
    a041.to_excel(writer, sheet_name='ANA13B041', index=False)
    a050.to_excel(writer, sheet_name='ANA13B050', index=False)
    a061.to_excel(writer, sheet_name='ANA13B061', index=False)
    a080.to_excel(writer, sheet_name='ANA13B080', index=False)
    a089.to_excel(writer, sheet_name='ANA13B089', index=False)
    a103.to_excel(writer, sheet_name='ANA13B103', index=False)
   

    writer.save() 

print ('Done')

