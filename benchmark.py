#!/usr/bin/env python
# coding: UTF-8

import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np

csvfile = "UnixBench.csv"

df = pd.read_csv(csvfile, index_col=0)

def make_chart(idx):

    title = df.index[idx]
    df2 = df.loc[title]
	
    cols = len(df2)
    index = [df2.index[i] for i  in range(0, cols, 2)]
    index = [re.sub(" / [0-9 CPU]*", "", str) for str in index]
    single = [df2[i] for i  in range(0, cols, 2)]
    many = [df2[i] for i  in range(1, cols, 2)]
	
    fig = plt.figure(figsize=(10, 3.2))
	
    bar_width = 0.45
    x = np.arange(len(index))
	
    plt.title(title)
    plt.barh(x - bar_width/2, single, bar_width, color="tab:blue", label="single core")
    plt.barh(x + bar_width/2, many, bar_width, color="tab:orange", label="many core")
    plt.legend()
    plt.subplots_adjust(left=0.25, right=0.98)
    plt.gca().invert_yaxis() # 上下並びを逆順に
    plt.yticks(x, index)
    plt.grid(axis='x')
    plt.pause(5)
    fig.savefig("images/" + str(idx) + ".png")

##
##
##
for i in range(len(df)):
    make_chart(i)

# import pdb; pdb.set_trace()

### Local Variables: ###
### truncate-lines:t ###
### End: ###


