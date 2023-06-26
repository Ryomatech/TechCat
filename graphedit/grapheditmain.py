import numpy as np
import matplotlib.pyplot as plt
import scienceplots
import pandas as pd

data_file_name="16-B.csv"
save_file_name="savefile.pdf"

csv_df = pd.read_csv(data_file_name,header=None)


x = csv_df[csv_df.columns[0]]
y1 = csv_df[csv_df.columns[1]]

x=[1,2,3,4,5]
y=[1,2,3,4,5]

with plt.style.context(['science']):
    fig = plt.figure()
    plt.plot(x,y,marker=".",linestyle="-", color="purple",label='aaa')
    plt.xlim(0, 180)
    plt.ylim(2,1000)
    plt.xlabel("bbb",fontsize=13)
    plt.ylabel('aaa',fontsize=13) 
    plt.legend(fontsize=5)
    plt.show() 
    plt.savefig(save_file_name) 













