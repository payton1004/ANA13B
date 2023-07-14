import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import datetime
import string
from scipy.stats import linregress

def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')

# 0 '2020-12-10', 
# 1 '2020-12-16', 
# 2 '2020-12-21', # broken
# 3 '2020-12-23', 
# 4 '2021-01-06', # broken
# 5 '2021-01-23', 
# 6 '2021-01-30'  # broken

print("i: index of run date")
i = int(input("i = "))

# raw data directory
_folder='/Users/jung-ok/work1/ANA11/raw_data/winkler/'

### Blank 
# file name: 'blank.csv'
_blk = pd.read_csv(_folder+'blank.csv', index_col=None,  parse_dates=[0])

# 'Date (UTC)', 'R1', 'R2', 'R1-R2', 'set', 'remarks'
_date=_blk['Date (UTC)'].unique()

print(_blk[_blk['Date (UTC)']==_date[i]])

# year, month, day
_y=str(_date[i])[:4]
_m=str(_date[i])[5:7]
_d=str(_date[i])[8:10]

# plot directory
_folder='/Users/jung-ok/work1/ANA11/plot/winkler/'

# figsize(float, float), default: rcParams["figure.figsize"] (default: [6.4, 4.8])
plt.rcParams["figure.figsize"] = (8*1.3,6*1.3)

# bar graph
ind = np.arange(len(_blk[_blk['Date (UTC)']==_date[i]])) # the x locations for the groups
width = 0.15  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind-width , _blk[_blk['Date (UTC)']==_date[i]]['R1'], width, label='R1', color='blue')
rects2 = ax.bar(ind , _blk[_blk['Date (UTC)']==_date[i]]['R2'], width, label='R2', color='orange')
rects3 = ax.bar(ind+width , _blk[_blk['Date (UTC)']==_date[i]]['R1-R2'], width, label='R1-R2', color='green')
# ax.set_ylabel('Scores')
ax.set_title(str(_date[i])[:10]) #'2020-12-10'
# ax.set_xticks(ind)
# ax.set_xticklabels(('1', '2', '3', '4', '5'))
ax.set_xticks([])
ax.set_xticklabels([])

ax.legend()

autolabel(rects1, "left")
autolabel(rects2, "center")
autolabel(rects3, "right")

fig.tight_layout()
plt.savefig(_folder+'blk_'+_y+_m+_d+'.png')
plt.show()



    


