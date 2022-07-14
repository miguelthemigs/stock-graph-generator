import tkinter as tk
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt

# tkinter
HEIGHT = 700
WIDTH = 1000

root = tk.Tk() # window

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH) # screen size
canvas.pack()

bg_image = tk.PhotoImage(file='stock-market-3 (Personalizado).png')
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# caption
canvas = tk.Canvas(root, width=1000, height= 750, bg="light blue")
canvas.create_text(250, 12, text="US Stock:(US) | Brazilian Stock:(BS) | Crypto:(C)", font=('Courier', 14))
canvas.place(x=230, y=10, width=540, height=50)

# type of item 
frame_type = tk.Frame(root, bg='black', bd=10)
frame_type.place(x=130, y=40, width=700, height=70)

entry_type = tk.Entry(frame_type, font=('Courier', 18))
entry_type.place(relx= 0.35, relwidth=0.65, relheight=1)

label_type = tk.Label(frame_type, font=('Courier', 12), text='Enter the type: \n US, BS or C:')
label_type.place(relx=0, relwidth=0.34, relheight=1)

# ticker
frame_ticker = tk.Frame(root, bg='black', bd=10)
frame_ticker.place(x=130, y=150, width=700, height=70)

entry_ticker = tk.Entry(frame_ticker, font=('Courier', 18))
entry_ticker.place(relx= 0.35, relwidth=0.65, relheight=1)

label_ticker = tk.Label(frame_ticker, font=('Courier', 12), text='Enter the ticker:')
label_ticker.place(relx=0, relwidth=0.34, relheight=1)

# start date
frame_start_date = tk.Frame(root, bg='black', bd=10)
frame_start_date.place(x=130, y=280, width=700, height=70)

entry_start_date = tk.Entry(frame_start_date, font=('Courier', 18))
entry_start_date.place(relx= 0.35, relwidth=0.65, relheight=1)

label_start_date = tk.Label(frame_start_date, font=('Courier', 12), text='Enter the start date: \n (mm/dd/aa)')
label_start_date.place(relx=0, relwidth=0.34, relheight=1)

# end date
frame_end_date = tk.Frame(root, bg='black', bd=10)
frame_end_date.place(x=130, y=410, width=700, height=70)

entry_end_date = tk.Entry(frame_end_date, font=('Courier', 18))
entry_end_date.place(relx= 0.35, relwidth=0.65, relheight=1)

label_end_date = tk.Label(frame_end_date, font=('Courier', 12), text='Enter the end date: \n (mm/dd/aa)')
label_end_date.place(relx=0, relwidth=0.34, relheight=1)

# running code
def get_graph(entry_type, entry_start_date, entry_end_date, entry_ticker):
    if entry_type in ['BS', 'bs'] :
        entry_ticker = f'{entry_ticker}.SA'
    elif entry_type in ['C', 'c']:
        entry_ticker = f'{entry_ticker}-USD'

    price = web.DataReader(entry_ticker.upper(), data_source='yahoo', start=entry_start_date, end=entry_end_date)
    price['Adj Close'].plot(figsize=(12,7))
    plt.show()

# button
main_button = tk.Button(root, text='Generate Graph', font=('Courier', 18), command=lambda:get_graph(entry_type.get(), entry_start_date.get(), entry_end_date.get(), entry_ticker.get()))
main_button.place(x=300, y=530, width=350, height=100)
root.mainloop()