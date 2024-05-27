
# -*- coding: utf-8 -*-

from ttkwidgets import Table
import tkinter as tk
from tkinter import ttk

def tableFrame(root, frame, dataGener, columns):
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    style = ttk.Style(root)
    style.theme_use('clam')
    style.configure(root,background='DarkGray')
    sortable = tk.BooleanVar(root, False)


    table = Table(frame, columns=columns, sortable=sortable.get(), height=30)
    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=300, stretch=False)

    # sort column A content as int instead of strings
    table.column(columns[0], type=int)

    for i in dataGener():
        table.insert('', 'end', iid=i,
                     values=i)

    # toggle table properties
    def toggle_sort():
        table.config(sortable=sortable.get())

    tk.Checkbutton(frame, text='sortable', variable=sortable, command=toggle_sort).pack(side='bottom')
    table.pack(anchor=tk.W)
