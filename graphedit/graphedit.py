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





def main(data,x_index,y_indexs,X_name,Y_name,X_min,X_max,Y_min,Y_max,X_orlog,Y_orlog,legend_oron,save_file_name,file_dpi,element_names,element_points,element_lines):
    x=data[data.columns[x_index]]
    if len(y_indexs) == 1:
        colors = ['black']
    else:
        colors = ['#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd','#8c564b','#e377c2']
    fig, ax = plt.subplots()
    with plt.style.context(['science','ieee',"no-latex"]):
        for i in range(len(y_indexs)):
            ax.plot(x,data[data.columns[y_indexs[i]]],marker=element_points[i],linestyle=element_lines[i], color=colors[i],label=element_names[i])
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



















