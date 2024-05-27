import tkinter as tk
from tkinter import ttk

def componentUsaged(root, frame, dataGener, position, description):
    lbl = ttk.Label(frame, font=('Times New Romans', 22, 'bold'))
    dataGener(lbl, description)
    lbl.pack(anchor=position)