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
        data = pd.read_csv(file_path)
        global df
        df = data

def close_data_row_window():
    data_row_window.destroy()





def data_row_select():
    labels=[]

    global data_row_window
    data_row_window = tk.Toplevel()
    data_row_window.title("")
    data_row_window.overrideredirect(False)
    data_row_window.geometry("500x500")
    data_row_window.configure(bg="#444654")

    def change_label_color(event):
        global x_index
        global y_index
        current_label = event.widget  # イベントが発生したラベルを取得
        label_index = labels.index(current_label) 
        if current_label.cget("background") == '#ffffff':
            event.widget.config(background="#b0c4de")
            x_index = label_index
        elif current_label.cget("background") == '#b0c4de':
            event.widget.config(background="#ffb6c1")
            y_index = label_index
        else:
            event.widget.config(background="#ffffff")
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
    close_data_row_window_button.grid(row=1, column=column_count,padx=6, pady=10,ipady=10)
    data_row_window.mainloop()

def generate_graph():
    graphedit.main(df[df.columns[x_index]],df[df.columns[y_index]])
    print(x_index)
    print(y_index)
    print(df[df.columns[x_index]])
    print(df[df.columns[y_index]])

def quit_program():
    sys.exit(1)


# Tkinterウィンドウの作成
root = tk.Tk()
root.title("Graph Editor")
root.geometry("700x700")
root.overrideredirect(False)
root.resizable(0, 0)    
root.configure(bg="#444654")
root.iconbitmap("favicon.ico")


image_path = "aaaa.png"

if os.path.isfile(image_path):
    # PNG画像を読み込み
    image = Image.open(image_path)
    # 画像をTkinter用のイメージオブジェクトに変換
    tk_image = ImageTk.PhotoImage(image)
    # 画像を表示するラベルを作成
    viewer_label = tk.Label(root, image=tk_image)
else:
    viewer_label = tk.Label(root, text='No Image',bd=0.5,font=("",50),bg="#40414f",width=20,height=2,fg='#fefefe',highlightthickness=0, justify="center",relief="solid")


csv_file_button = tk.Button(root, text="Select CSV", command=load_csv)
data_row_select_button = tk.Button(root, text="データ列選択", command=data_row_select)
generate_button = tk.Button(root, text="生成",command=generate_graph)
quit_button = tk.Button(root, text="終了",command=quit_program)




csv_file_button.config(width=5, height=1, bg="#444654", fg="#444654", bd=0, relief="flat", activebackground="#555555", activeforeground="#444654",cursor="hand")
data_row_select_button.config(width=5, height=1, bg="#444654", fg="#444654", bd=0, relief="flat", activebackground="#555555", activeforeground="#444654",cursor="hand")
generate_button.config(width=5, height=1, bg="#444654", fg="#444654", bd=0, relief="flat", activebackground="#555555", activeforeground="#444654",cursor="hand")
quit_button.config(width=5, height=1, bg="#444654", fg="#444654", bd=0, relief="flat", activebackground="#555555", activeforeground="#444654",cursor="hand")



csv_file_button.grid(row=0, column=0, padx=6, pady=10,ipady=10)
data_row_select_button.grid(row=1, column=0, padx=6, pady=10,ipady=10)
viewer_label.grid(row=2, column=0, padx=6, pady=10,ipady=0)
generate_button.grid(row=3, column=0,padx=6, pady=10,ipady=10)
quit_button.grid(row=4, column=0,padx=6, pady=10,ipady=10)

# Tkinterウィンドウのメインループ
root.mainloop()