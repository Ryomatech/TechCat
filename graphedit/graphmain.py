import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import graphedit





window = tk.Tk()
window.title("Matplotlibグラフ")
window.geometry("800x700")
window.overrideredirect(False)
window.resizable(0, 0)
window.configure(bg="#444654")
window.iconbitmap("favicon.ico")

# グラフを表示するフレームを作成
frame = tk.Frame(window)
frame.pack()

# キャンバスを作成しFigureを埋め込む
canvas = tk.Canvas(window, width=400, height=300)
#canvas.draw()


# キャンバスをウィンドウに配置
#canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)

# Tkinterウィンドウを表示
window.mainloop()