import tkinter as tk
import molcal
import csv
from tkinter import ttk
import os
from tkinter import filedialog
import sys





history = []
global filename

root = tk.Tk()


root.title("分子量計算")
root.geometry("500x500")
root.overrideredirect(False)
root.resizable(0, 0)
root.configure(bg="#444654")
root.iconbitmap("favicon.ico")


def update_output():
    input_text = entry.get()  # 入力された文字列を取得
    processed_text = process_string(input_text)  # 入力文字列を処理する
    result_label.config(text=processed_text)  # 処理結果を表示

def process_string(input_text):
    processed_text=molcal.molcalcal(input_text)
    return processed_text

def copy_text():
    input_text = entry.get()
    processed_text = process_string(input_text)
    root.clipboard_clear()
    root.clipboard_append(processed_text)

def add_to_history():
    input_text = entry.get()
    processed_text = process_string(input_text)
    text = entry.get()+','+processed_text # 入力された文字列を取得
    history.append(text)  # 履歴に追加
    update_label()

def update_label():
    history_text = '\n'.join(history)  # 履歴の文字列を改行区切りに連結
    history_label.config(text=history_text)



def history_save():
    lines=history
    dialog=dirdialog_ask()
    csv_name=dialog+'/'+get_filename()+'.csv'
    with open(csv_name, 'w', newline='') as file:
        writer = csv.writer(file)
        # ヘッダ行を書き込む
        writer.writerow(['化学式','分子量'])
        # データ行を書き込む
        for line in lines[0:]:
            data = line.split(',')
            writer.writerow(data)
    close_csv_save()

def dirdialog_ask():
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = filedialog.askdirectory(initialdir = iDir)
    return iDirPath

def close_csv_save():
    save_window.destroy()

def get_history():
    return history

def quit_program():
    sys.exit(1)

def open_save_window():
    global save_window
    save_window = tk.Toplevel()
    save_window.title("")
    save_window.overrideredirect(False)
    save_window.resizable(0, 0)
    save_window.geometry("200x140")
    save_window.configure(bg="#444654")
    save_title=tk.Label(save_window,text="保存ファイル名",bd=0.5,font=("",20),bg="#444654",fg='#fefefe',highlightthickness=0, justify="center",relief="flat")    
    global filename_entry
    filename_entry=tk.Entry(save_window,bd=0.5,font=("",15),bg="#fefefe",width=15,fg='#444654',highlightthickness=0, justify="center",relief="solid")
    filename_entry.focus_set() 
    dotcsv=tk.Label(save_window,text=".csv",bd=0.5,font=("",15),bg="#444654",fg='#fefefe',highlightthickness=0, justify="center",relief="flat")
    save_file_button = tk.Button(save_window, text="保存",command=history_save)
    save_file_button.config(width=6, height=2, bg="#444654", fg="#444654", bd=0, relief="flat", activebackground="#555555", activeforeground="#444654",cursor="hand")
    
    save_title.grid(row=0, column=0, padx=6, pady=5)
    filename_entry.grid(row=1, column=0, padx=6, pady=5)
    dotcsv.grid(row=1, column=1, padx=0, pady=0, sticky=tk.SW)
    save_file_button.grid(row=3, column=0, padx=6, pady=5)

    save_window.mainloop()

def clear_entry():
    entry.delete(0, tk.END)  # Entryのテキストを先頭から末尾まで削除


def get_filename():
    return filename_entry.get()

def vanish_history():
    history.clear()
    history_label.config(text='')

def disable_entry_focus(event):
    return "break"


clear_button = tk.Button(root, text="クリア",command=clear_entry)

#entry = tk.Entry(root,bd=0.5,font=("",30),bg="#40414f",width=20,fg='#fefefe',highlightthickness=0, justify="center",relief="solid")
entry = ttk.Entry(root,width=20,font=("",30), justify="center")
entry.focus_set() 

entry.bind("<KeyRelease>", lambda event: update_output())

result_label = tk.Label(root, bd=0.5,font=("",30),bg="#40414f",width=20,height=2,fg='#fefefe',highlightthickness=0, justify="center",relief="solid")

copy_button = tk.Button(root,text="コピー", command=copy_text)

history_button = tk.Button(root,text="履歴に追加", command=add_to_history)

history_vanish =tk.Button(root, text="履歴を消去",command=vanish_history)

save_csv_button = tk.Button(root, text="履歴をCSVファイルとして保存",command=open_save_window)

history_label = tk.Label(root, bd=0.5,font=("",30),bg="#40414f",width=20,fg='#fefefe',highlightthickness=0, justify="center",relief="solid")

quit_button = tk.Button(root, text="終了",command=quit_program)

style = ttk.Style()
style.configure('Custom.TEntry', borderwidth=0,foreground="#fefefe",fieldbackground=[("#40414f")],selectbackground=[("#40414f")], insertcolor='#fefefe',highlightthickness=0,relief="solid")

# スタイルを適用
entry.configure(style='Custom.TEntry')

clear_button.config(width=6, height=2, bg="#444654", fg="#444654", bd=0, relief="flat", activebackground="#555555", activeforeground="#444654",cursor="hand")
copy_button.config(width=6, height=2, bg="#444654", fg="#444654", bd=0, relief="flat", activebackground="#555555", activeforeground="#444654",cursor="hand")
history_button.config(width=10, height=2, bg="#444654", fg="#444654", bd=0, relief="flat", activebackground="#555555", activeforeground="#444654",cursor="hand")
history_vanish.config(width=10, height=2, bg="#444654", fg="#444654", bd=0, relief="flat", activebackground="#555555", activeforeground="#444654",cursor="hand")
save_csv_button.config(width=20, height=2, bg="#444654", fg="#444654", bd=0, relief="flat", activebackground="#555555", activeforeground="#444654",cursor="hand")
quit_button.config(width=10, height=2, bg="#444654", fg="#444654", bd=0, relief="flat", activebackground="#555555", activeforeground="#444654",cursor="hand")

entry.grid(row=0, column=0, padx=6, pady=10,ipady=20,columnspan=2)
clear_button.grid(row=0, column=2, padx=6, pady=10)
result_label.grid(row=1, column=0, padx=6, pady=10, columnspan=2)
copy_button.grid(row=1, column=2, padx=6, pady=10) 
history_button.grid(row=2, column=0, padx=6, pady=10)
history_vanish.grid(row=2, column=1, padx=6, pady=10)
save_csv_button.grid(row=3, column=0, padx=6, pady=10)
history_label.grid(row=4, column=0, padx=6, pady=10, columnspan=2)
quit_button.grid(row=5, column=0, padx=6, pady=10,columnspan=2)

entry.bind("<FocusIn>", disable_entry_focus)

root.mainloop()