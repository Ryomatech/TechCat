import tkinter as tk
from PIL import ImageTk, Image
import os
from tkinter import filedialog
import pandas as pd
from tkinter import ttk
import graphedit
import sys



def load_csv():
    # ファイルダイアログを開いてCSVファイルを選択
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        # CSVファイルを読み込む
        data = pd.read_csv(file_path,names=('x','y'))
        global df
        df = data

def close_data_row_window():
    global click_count
    X_min_entry.delete(0, "end")
    X_max_entry.delete(0, "end")
    Y_min_entry.delete(0, "end")
    Y_max_entry.delete(0, "end")

    X_min_entry.insert(0, str(df[df.columns[x_index]].min())[:5]) 
    X_max_entry.insert(0, str(df[df.columns[x_index]].max())[:5]) 
    Y_min_entry.insert(0, str(df[df.columns[y_index]].min())[:5]) 
    Y_max_entry.insert(0, str(df[df.columns[y_index]].max())[:5]) 
    click_count=0
    data_row_window.destroy()

def remove_result_png():
    if os.path.exists('result.png'):
        os.remove('result.png')





def change_label_color(event):
        global click_count
        global x_index
        global y_index
        current_label = event.widget  # イベントが発生したラベルを取得
        label_index = labels.index(current_label) 
        if click_count==0:
            event.widget.config(background="#ffb6c1")
            x_index = label_index
        elif click_count==1:
            event.widget.config(background="#b0c4de")
            y_index = label_index
        else:
            event.widget.config(background="#ffffff")
        click_count += 1


def data_row_select():
    global labels
    labels=[]
    global data_row_window
    data_row_window = tk.Toplevel()
    data_row_window.title("")
    data_row_window.overrideredirect(False)
    data_row_window.geometry("550x500")
    data_row_window.configure(bg="#444654")
    if 'df' in globals():
        column_count = df.shape[1]
        for i, column in enumerate(df.columns):
            values = df[column].tolist()
            values_str = "\n".join(str(value) for value in values)
            label='label'+str(i)
            label = tk.Label(data_row_window, text=f"{column}\n{values_str}",bd=0.5,highlightthickness=0,relief="solid",background='#ffffff')
            label.grid(row=1, column=i)
            label.bind("<Button-1>", change_label_color)
            labels.append(label) 
    else:                                                       
        label = tk.Label(data_row_window, text='csvファイルを選択してね', justify='left')
        label.grid(row=1, column=0)

    close_data_row_window_button = tk.Button(data_row_window, text="閉じる",command=close_data_row_window)
    close_data_row_window_button.config(width=5, height=1, bg="#444654", fg="#444654", bd=0, relief="flat", activebackground="#555555", activeforeground="#444654",cursor="hand")
    close_data_row_window_button.grid(row=1, column=column_count,padx=6, pady=10,ipady=10,sticky=tk.N)
    data_row_window.mainloop()

def generate_graph():
    graphedit.main(df[df.columns[x_index]],df[df.columns[y_index]],X_name_entry.get(),Y_name_entry.get(),int(X_min_entry.get()),int(X_max_entry.get()),int(Y_min_entry.get()),int(Y_max_entry.get()),X_axis_var.get(),Y_axis_var.get(),legend_var.get(),"result.png",100)
    update_label()



def quit_program():
    sys.exit(1)

def dirdialog_ask():
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = filedialog.askdirectory(initialdir = iDir)
    return iDirPath


def validate_input(text):
    if len(text) <= 5:
        return True
    else:
        return False

def save_as_pdf():
    save_file_name = save_name_entry.get()+'.pdf'
    dialog=dirdialog_ask()
    save_place=dialog+'/'+save_file_name
    graphedit.main(df[df.columns[x_index]],df[df.columns[y_index]],X_name_entry.get(),Y_name_entry.get(),int(X_min_entry.get()),int(X_max_entry.get()),int(Y_min_entry.get()),int(Y_max_entry.get()),X_axis_var.get(),Y_axis_var.get(),legend_var.get(),"temp.png",1000)
    image = Image.open('temp.png')
    image.save(save_place, "PDF", resolution=100.0, quality=100)
    os.remove('temp.png')

def save_as_png():
    save_file_name = save_name_entry.get()+'.png'
    dialog=dirdialog_ask()
    save_place=dialog+'/'+save_file_name
    graphedit.main(df[df.columns[x_index]],df[df.columns[y_index]],X_name_entry.get(),Y_name_entry.get(),int(X_min_entry.get()),int(X_max_entry.get()),int(Y_min_entry.get()),int(Y_max_entry.get()),X_axis_var.get(),Y_axis_var.get(),legend_var.get(),save_place,1000)





# Tkinterウィンドウの作成
root = tk.Tk()
root.title("Graph Editor")
root.geometry("900x700")
root.overrideredirect(False)
#root.resizable(0, 0)    
root.configure(bg="#444654")
root.iconbitmap("fav    icon.ico")
viewer_label = tk.Label(root)

validation = root.register(validate_input)

click_count=0

def update_label():
    image_path = "result.png"
    if os.path.isfile(image_path):
        # PNG画像を読み込み
        image = Image.open(image_path)
        # 画像をTkinter用のイメージオブジェクトに変換
        tk_image = ImageTk.PhotoImage(image)
        # 画像を表示するラベルを作成
        viewer_label.config(image=tk_image,width=600,height=400,bg="#40414f")
        viewer_label.image = tk_image
    else:
        viewer_label.config(text='No Image',bd=0.5,font=("",50),bg="#40414f",width=19,height=7,fg='#fefefe',highlightthickness=0, justify="center",relief="solid")



csv_file_button = tk.Button(root, text="CSV選択", command=load_csv)
data_row_select_button = tk.Button(root, text="データ列選択", command=data_row_select)
generate_button = tk.Button(root, text="生成",command=generate_graph)
quit_button = tk.Button(root, text="終了",command=quit_program)
PDF_save_button = tk.Button(root, text="PDFとして保存",command=save_as_pdf)
PNG_save_button = tk.Button(root, text="PNGとして保存",command=save_as_png)


X_label=tk.Label(root,text="X軸設定",bd=0.5,font=("",20),bg="#444654",fg='#fefefe',highlightthickness=0, justify="center",relief="flat") 
X_label_name=tk.Label(root,text="ラベル名",bd=0.5,font=("",14),bg="#444654",fg='#fefefe',highlightthickness=0, justify="center",relief="flat") 
X_name_entry = tk.Entry(root,width=8)
X_min_label=tk.Label(root,text="最小値",bd=0.5,font=("",14),bg="#444654",fg='#fefefe',highlightthickness=0, justify="center",relief="flat") 
X_min_entry = tk.Entry(root,width=5, validate="key", validatecommand=(validation, '%P'))
X_max_label=tk.Label(root,text="最大値",bd=0.5,font=("",14),bg="#444654",fg='#fefefe',highlightthickness=0, justify="center",relief="flat") 
X_max_entry = tk.Entry(root,width=5, validate="key", validatecommand=(validation, '%P'))
X_axis_var = tk.StringVar(value="linear")
X_linear_radio = tk.Radiobutton(root, text="通常軸", variable=X_axis_var, value="linear",bg="#444654",fg='#fefefe')
X_log_radio = tk.Radiobutton(root, text="対数軸", variable=X_axis_var, value="log",bg="#444654",fg='#fefefe')

Y_label=tk.Label(root,text="Y軸設定",bd=0.5,font=("",20),bg="#444654",fg='#fefefe',highlightthickness=0, justify="center",relief="flat") 
Y_label_name=tk.Label(root,text="ラベル名",bd=0.5,font=("",14),bg="#444654",fg='#fefefe',highlightthickness=0, justify="center",relief="flat") 
Y_name_entry = tk.Entry(root,width=8)
Y_min_label=tk.Label(root,text="最小値",bd=0.5,font=("",14),bg="#444654",fg='#fefefe',highlightthickness=0, justify="center",relief="flat") 
Y_min_entry = tk.Entry(root,width=5, validate="key", validatecommand=(validation, '%P'))
Y_max_label=tk.Label(root,text="最大値",bd=0.5,font=("",14),bg="#444654",fg='#fefefe',highlightthickness=0, justify="center",relief="flat") 
Y_max_entry = tk.Entry(root,width=5, validate="key", validatecommand=(validation, '%P'))
Y_axis_var = tk.StringVar(value="linear")
Y_linear_radio = tk.Radiobutton(root, text="通常軸", variable=Y_axis_var, value="linear",bg="#444654",fg='#fefefe')
Y_log_radio = tk.Radiobutton(root, text="対数軸", variable=Y_axis_var, value="log",bg="#444654",fg='#fefefe')

legend_label=tk.Label(root,text="凡例設定",bd=0.5,font=("",20),bg="#444654",fg='#fefefe',highlightthickness=0, justify="center",relief="flat") 
legend_var = tk.StringVar(value="on")
legend_on_radio = tk.Radiobutton(root, text="凡例あり", variable=legend_var, value="on",bg="#444654",fg='#fefefe')
legend_off_radio = tk.Radiobutton(root, text="凡例なし", variable=legend_var, value="off",bg="#444654",fg='#fefefe')

save_label=tk.Label(root,text="保存設定",bd=0.5,font=("",20),bg="#444654",fg='#fefefe',highlightthickness=0, justify="center",relief="flat") 
save__name_label=tk.Label(root,text="ファイル名",bd=0.5,font=("",14),bg="#444654",fg='#fefefe',highlightthickness=0, justify="center",relief="flat") 
save_name_entry = tk.Entry(root,width=8)
save__type_label=tk.Label(root,text=".pdf or .png",bd=0.5,font=("",10),bg="#444654",fg='#fefefe',highlightthickness=0, justify="center",relief="flat") 

remove_result_png()
update_label()


csv_file_button.config(width=5, height=1, bg="#444654", fg="#444654", bd=0, relief="flat", activebackground="#555555", activeforeground="#444654",cursor="hand")
data_row_select_button.config(width=5, height=1, bg="#444654", fg="#444654", bd=0, relief="flat", activebackground="#555555", activeforeground="#444654",cursor="hand")
generate_button.config(width=5, height=1, bg="#444654", fg="#444654", bd=0, relief="flat", activebackground="#555555", activeforeground="#444654",cursor="hand")
quit_button.config(width=5, height=1, bg="#444654", fg="#444654", bd=0, relief="flat", activebackground="#555555", activeforeground="#444654",cursor="hand")
PDF_save_button.config(width=7, height=1, bg="#444654", fg="#444654", bd=0, relief="flat", activebackground="#555555", activeforeground="#444654",cursor="hand")
PNG_save_button.config(width=7, height=1, bg="#444654", fg="#444654", bd=0, relief="flat", activebackground="#555555", activeforeground="#444654",cursor="hand")



csv_file_button.grid(row=0, column=5, padx=6, pady=10,ipady=10)
data_row_select_button.grid(row=0, column=6, padx=6, pady=10,ipady=10)
viewer_label.grid(row=1, column=0, padx=6, pady=10,ipady=0,columnspan=10,rowspan=40)


X_label.grid(row=1, column=11, padx=6, pady=10,ipady=0)
X_label_name.grid(row=2, column=11,sticky=tk.E)
X_name_entry.grid(row=2, column=12,sticky=tk.W)
X_min_label.grid(row=3, column=11,sticky=tk.E)
X_min_entry.grid(row=3, column=12,sticky=tk.W)
X_max_label.grid(row=3, column=13)
X_max_entry.grid(row=3, column=14)
X_linear_radio.grid(row=4, column=11)
X_log_radio.grid(row=5, column=11)


Y_label.grid(row=16, column=11, padx=6, pady=10,ipady=0)
Y_label_name.grid(row=17, column=11,sticky=tk.E)
Y_name_entry.grid(row=17, column=12,sticky=tk.W)
Y_min_label.grid(row=18, column=11,sticky=tk.E)
Y_min_entry.grid(row=18, column=12,sticky=tk.W)
Y_max_label.grid(row=18, column=13)
Y_max_entry.grid(row=18, column=14)
Y_linear_radio.grid(row=19, column=11)
Y_log_radio.grid(row=20, column=11)

legend_label.grid(row=22, column=11, padx=6, pady=10,ipady=0)
legend_on_radio.grid(row=23, column=11)
legend_off_radio.grid(row=24, column=11)

save_label.grid(row=30, column=11)
save__name_label.grid(row=31, column=11,sticky=tk.E)
save_name_entry.grid(row=31, column=12)
save__type_label.grid(row=31, column=13,sticky=tk.SW)


generate_button.grid(row=41, column=0,padx=6, pady=10,ipady=10)
PDF_save_button.grid(row=41, column=1,padx=6, pady=10,ipady=10)
PNG_save_button.grid(row=41, column=2,padx=6, pady=10,ipady=10)
quit_button.grid(row=41, column=3,padx=6, pady=10,ipady=10)


root.mainloop()