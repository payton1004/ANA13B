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
        ax1.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')
        ax2.annotate('{}'.format(height),
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
# ind = np.arange(len(_blk[_blk['Date (UTC)']==_date[i]])) # the x locations for the groups
ind = _blk[_blk['Date (UTC)']==_date[i]].reset_index().index 
width = 0.15  # the width of the bars


# fig, ax = plt.subplots()
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
# fig.subplots_adjust(hspace=0.25)  # adjust space between axes

# hide the spines between ax and ax2
ax1.spines['bottom'].set_visible(False)
# ax1.tick_params(labeltop=False)  # don't put tick labels at the top
ax1.tick_params(axis='x',which='both',bottom=False)
ax2.spines['top'].set_visible(False)
# ax1.xaxis.tick_top()
# ax2.xaxis.tick_bottom()
ax2.set_xticks([])
ax2.set_xticklabels([])

# zoom-in / limit the view to different portions of the data

# if i==2:
#     y2_low=0 ; y2_high=102
#     y1_low=228 ; y1_high=320
if i==2:
    y2_low=0 ; y2_high=92
    y1_low=103 ; y1_high=320    
# elif i==4:
#     y2_low=0 ; y2_high=116
#     y1_low=422 ; y1_high=510
elif i==4:
    y2_low=0 ; y2_high=92
    y1_low=103 ; y1_high=510    
elif i==6:
    y2_low=0 ; y2_high=92
    y1_low=103; y1_high=310        

ax2.set_ylim(y2_low, y2_high)  # most of the data
ax1.set_ylim(y1_low, y1_high)  # outliers only

# ax1.set_yticks(np.arange(230,321,20))


# plot the same data on both axes
rects1_1 = ax1.bar(ind-width , _blk[_blk['Date (UTC)']==_date[i]]['R1'], width, label='R1', color='blue')
rects2_1 = ax1.bar(ind,        _blk[_blk['Date (UTC)']==_date[i]]['R2'], width, label='R2', color='orange')
rects3_1 = ax1.bar(ind+width , _blk[_blk['Date (UTC)']==_date[i]]['R1-R2'], width, label='R1-R2', color='green')

rects1_2 = ax2.bar(ind-width , _blk[_blk['Date (UTC)']==_date[i]]['R1'], width, label='R1', color='blue')
rects2_2 = ax2.bar(ind, _blk[_blk['Date (UTC)']==_date[i]]['R2'], width, label='R2', color='orange')
rects3_2 = ax2.bar(ind+width , _blk[_blk['Date (UTC)']==_date[i]]['R1-R2'], width, label='R1-R2', color='green')


# Now, let's turn towards the cut-out slanted lines.
# We create line objects in axes coordinates, in which (0,0), (0,1),
# (1,0), and (1,1) are the four corners of the axes.
# The slanted lines themselves are markers at those locations, such that the
# lines keep their angle and position, independent of the axes size or scale
# Finally, we need to disable clipping.

d = .5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)


# ax1.set_ylabel('$\mu$L')
ax1.set_title(str(_date[i])[:10]) #'2020-12-10'

ax1.legend()

autolabel(rects1_1, "left")
autolabel(rects2_1, "center")
autolabel(rects3_1, "right")

fig.tight_layout()
plt.savefig(_folder+'blk_'+_y+_m+_d+'.png')
plt.show()


