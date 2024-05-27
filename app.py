import tkinter as tk
from time import strftime
from tkinter import ttk

import psutil

from app_table_wiget import tableFrame
from componentUsaged import componentUsaged

from main import runningProcesses, showNetwork, FreeSpace

# root window
root = tk.Tk()
root.geometry('900x600')
root.title('Моніторинг')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=15, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=600, height=600)
frame2 = ttk.Frame(notebook, width=600, height=600)
frame3 = ttk.Frame(notebook, width=600, height=600)
frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)

# add frames to notebook
notebook.add(frame1, text='Моніторинг ресурсів')
notebook.add(frame2, text='Процеси')
notebook.add(frame3, text='Мережі')



tableFrame(root=root,frame=frame3,
           dataGener=showNetwork,
           columns = ["Опис", "MAC-адреса", "IP-адреса"])

tableFrame(root=root,frame=frame2,
           dataGener=runningProcesses,
           columns = ["ід", "ім'я", "Віртуальний розмір (VirtualSize)"])





def time(label, description):
    string = description + strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time, label, description)

def ramUsed():
    return psutil.virtual_memory().percent


def ram(label, description):
    string = description + str(ramUsed()) + '%'
    label.config(text=string)
    label.after(1000, ram, label, description)

def cpuUsed():
    yield psutil.cpu_percent(interval=None, percpu=False)


def cpu(label, description):
    string = description + str(next(cpuUsed())) + '%'
    label.config(text=string)
    label.after(1000, cpu, label, description)




componentUsaged(root=root, frame=frame1,
                dataGener=time,
                position='w',
                description = 'ЧАС: ')

componentUsaged(root=root, frame=frame1,
                dataGener=ram,
                position='w',
                description='ОЗУ: ')

componentUsaged(root=root, frame=frame1,
                dataGener=cpu,
                position='w',
                description='ПРОЦЕСОР: ')


for i in FreeSpace():
    print(i)
    lbl = ttk.Label(frame1, text=i)
    lbl.pack(anchor="w")

root.mainloop()
