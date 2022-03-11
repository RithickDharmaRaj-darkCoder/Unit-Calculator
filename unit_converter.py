# Importing the Modules
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
from tkinter import ttk
from functools import partial

# Creating the main window
window = tk.Tk()
window.geometry('500x500')
window.title('Unit Converter')
window.configure(bg = 'gray')

# Creating the Fonts
font_head = font.Font(family='helvetica', size='25')
font1 = font.Font(family='helvetica', size='15')
font2 = font.Font(family='helvetica', size='20')

# [All Functions]
# Selected Function
def selected():
    pass

# From Function
def fromfunc():
    pass

# Creating the Unit Converter Label
lable_title = tk.Label(window, text='UNIT CONVERTER', bg='gray', fg='darkblue')
lable_title['font'] = font_head
lable_title.place(relx='0.48', rely='0.1', anchor='center')

# Creating Unit Lable
lable_unit = tk.Label(window, text='Unit', bg='gray', fg='black')
lable_unit['font'] = font1
lable_unit.place(relx='0.15', rely='0.25')

# Creating Unit Combobox
n = tk.StringVar()
combo_unit = ttk.Combobox(window, width=35, textvariable=n)
combo_unit.place(relx=0.5, rely=0.28, anchor='center')
combo_unit.current()
combo_unit.bind('<<ComboboxSelected>>', selected)

# Unit Combobox Values
combo_unit['values'] = ('Data Storage',
                    'Frequency',
                    'Length',
                    'Mass',
                    'Speed',
                    'Temperature',
                    'Volume',
                    'Time')


# Creating From Lable
lable_from = tk.Label(window, text='From', bg='gray', fg='black')
lable_from['font'] = font1
lable_from.place(relx=0.15, rely=0.37)

# Creating From Combobox
f = tk.StringVar()
combo_from = ttk.Combobox(window, width=35, textvariable=f)
combo_from.place(relx=0.5, rely=0.40, anchor='center')
combo_from.current()
combo_from.bind('<<ComboboxSelected>>', fromfunc)


# Creating MainLoop
window.mainloop()