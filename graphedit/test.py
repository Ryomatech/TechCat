import tkinter as tk

def change_label_color(event):
    current_color = event.widget.cget("background")  # イベントが発生したラベルの背景色を取得

    if current_color == "red":
        event.widget.config(background="blue")
    else:
        event.widget.config(background="red")

root = tk.Tk()
root.title("Label Color Change")

labels = []  # ラベルのリスト

for i in range(5):
    label = tk.Label(root, text="Label " + str(i+1), width=10, height=5, bg="red")
    label.pack(padx=20, pady=5)

    label.bind("<Button-1>", change_label_color)  # ラベルのクリックイベントを設定
    labels.append(label)  # ラベルをリストに追加

root.mainloop()
