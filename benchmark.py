#!/usr/bin/env python
# coding: UTF-8

import pandas as pd
import matplotlib.pyplot as plt

csvfile = "UnixBench.csv"

df = pd.read_csv(csvfile)
length = len(df)

def make_chart(idx):

    df2 = df.loc[idx]
    testname = df2[df2.index[0]]
    index = df2.index[1:]
    data = [df2[i] for i in index]
    colorlist = ["tab:blue" if i % 2 == 0 else "tab:orange" for i in range(len(data))]
    
    fig = plt.figure(figsize=(10, 2.5), dpi=100)

    plt.barh(index, data, color=colorlist)
    plt.grid(axis='x')
    plt.title(testname)
    plt.subplots_adjust(left=0.24, right=0.98)
    plt.gca().invert_yaxis() # 上下並びを逆順に

    plt.pause(5)
    # plt.show()
    fig.savefig("images/" + str(idx) + ".png")
    

for i in range(length):
    make_chart(i)
    
# import pdb; pdb.set_trace()

### Local Variables: ###
### truncate-lines:t ###
### End: ###


