import numpy as np
import matplotlib.pyplot as plt
import scienceplots
import pandas as pd




plt.rcParams['font.family'] = 'Hiragino Maru Gothic Pro'
plt.rcParams['figure.figsize'] = (6, 4)



def df_value():
    #csv_df=pd.read_csv(data_file_name)
    #x = csv_df[csv_df.columns[0]]
    #y = csv_df[csv_df.columns[1]]
    x=[1,2,3,4,5]
    y=[1,2,3,4,5]
    return x,y





def main(x,y,X_name,Y_name,X_min,X_max,Y_min,Y_max,X_orlog,Y_orlog,legend_oron,save_file_name,file_dpi):
    fig, ax = plt.subplots()
    with plt.style.context(['science','ieee',"no-latex"]):
        ax.plot(x,y,marker=".",linestyle="-", color="purple",label='Element1')
        ax.set_xlim(X_min, X_max)
        ax.set_ylim(Y_min,Y_max)
        ax.set_xlabel(X_name,fontsize=15)
        ax.set_ylabel(Y_name,fontsize=15) 
        if legend_oron=='on':
            ax.legend(fontsize=15)
        if X_orlog == 'log':
            ax.set_xscale("log")
        if Y_orlog == 'log':
            ax.set_yscale("log")
        #plt.show()
        fig.savefig(save_file_name,dpi=file_dpi) 
        #return fig



















