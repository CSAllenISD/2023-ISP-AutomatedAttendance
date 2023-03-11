import pandas as pd
import numpy as np
import tkinter as tk
from studentProfile import data

df = pd.read_csv('data.csv')
data = df.to_numpy()


teacher = input("Teacher Name: ")
classroom = input("Classroom Number: ")
subject = input("Subject: ")
roster = []


def on_click(data):
    roster.append(data)

root = tk.Tk()

button = tk.Button(root, text="Click me", command=on_click)
button.pack()

root.mainloop()

