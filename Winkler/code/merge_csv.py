import datetime
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import dates


# input file : 
#winkler04.py 실행 후 출력파일 
csv_files =sorted(glob('/Users/jung-ok/work1/ANA13B/processed/Winkler/LAB/DO*.csv'))
# print(csv_files)

df_concat = pd.concat([pd.read_csv(f) for f in csv_files ], ignore_index=True)
df_concat


# output_file='/Users/jung-ok/work1/ANA13B/processed/winkler/LAB/DO_winkler_CTD_ANA13B.csv'

# # Write the combined data to a new CSV file
# df_concat.to_csv(output_file, index=False)

print ('Done')

