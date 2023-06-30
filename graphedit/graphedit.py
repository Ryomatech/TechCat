import numpy as np
import matplotlib.pyplot as plt
import scienceplots
import pandas as pd


save_file_name="aaaa.png"

plt.rcParams['font.family'] = 'Hiragino Maru Gothic Pro'
plt.rcParams['figure.figsize'] = (6, 4)



def df_value():
    #csv_df=pd.read_csv(data_file_name)
    #x = csv_df[csv_df.columns[0]]
    #y = csv_df[csv_df.columns[1]]
    x=[1,2,3,4,5]
    y=[1,2,3,4,5]
    return x,y





def main(x,y):
    fig, ax = plt.subplots()
    with plt.style.context(['science','ieee',"no-latex"]):
        ax.plot(x,y,marker=".",linestyle="-", color="purple",label='aaa')
        ax.set_xlim(min(x), max(x))
        ax.set_ylim(min(y),max(y))
        ax.set_xlabel("あ",fontsize=15)
        ax.set_ylabel(ylabel='うう',fontsize=15) 
        ax.legend(fontsize=15)
        #plt.show()
        fig.savefig(save_file_name) 
        #return fig



















