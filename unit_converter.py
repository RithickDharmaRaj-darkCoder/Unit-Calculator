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
# Convert Function
def convert():
    pass

# Selected Function
def selected(event):
    unit = event.widget.get()
    if unit == 'Data Storage':
        combo_from['values'] = ('byte',
                                'KiloByte',
                                'MegaByte',
                                'GigaByte',
                                'TeraByte',
                                'PetaByte')
        combo_to['values'] = ('byte',
                              'KiloByte',
                              'MegaByte',
                              'GigaByte',
                              'TeraByte',
                              'PetaByte')
    elif unit == 'Frequency':
        combo_from['values'] = ()
        combo_to['values'] = ()
    elif unit == 'Length':
        combo_from['values'] = ('Millimeters',
                                'Centimeters',
                                'Decimeters',
                                'Meters',
                                'Kilometers')
        combo_to['values'] = ('Millimeters',
                              'Centimeters',
                              'Decimeters',
                              'Meters',
                              'Kilometers')
    elif unit == 'Mass':
        combo_from['values'] = ('Milligram',
                                'Centigram',
                                'Grams',
                                'Decigrams',
                                'Kilograms')
        combo_to['values'] = ('Milligram',
                              'Centigram',
                              'Grams',
                              'Decigrams',
                              'Kilograms')
    elif unit == 'Speed':
        combo_from['values'] = ()
        combo_to['values'] = ()
    elif unit == 'Temperature':
        combo_from['values'] = ()
        combo_to['values'] = ()
    elif unit == 'Volume':
        combo_from['values'] = ('Cubic Meters',
                                'Cubic Foot',
                                'Liters',
                                'Gallon',
                                'Cubic Centimeters')
        combo_to['values'] = ('Cubic Meters',
                              'Cubic Foot',
                              'Liters',
                              'Gallon',
                              'Cubic Centimeters')
    elif unit == 'Time':
        combo_from['values'] = ('Milliseconds',
                                'Seconds',
                                'Minutes',
                                'Hours',
                                'Days',
                                'Weeks',
                                'Months',
                                'Years')
        combo_to['values'] = ('Milliseconds',
                                'Seconds',
                                'Minutes',
                                'Hours',
                                'Days',
                                'Weeks',
                                'Months',
                                'Years')
    else:
        pass


# From Function
def fromfunc(event):
    global result_from
    result_from = event.widget.get()
    print(result_from)

# To Function
def tofunc(event):
    global result_to
    result_to = event.widget.get()
    print(result_to)

# Creating the Unit Converter Label
label_title = tk.Label(window, text='UNIT CONVERTER', bg='gray', fg='darkblue')
label_title['font'] = font_head
label_title.place(relx='0.5', rely='0.1', anchor='center')

# Creating Unit Lable
label_unit = tk.Label(window, text='Unit', bg='gray', fg='black')
label_unit['font'] = font1
label_unit.place(relx='0.18', rely='0.25')

# Creating Unit Combobox
n = tk.StringVar()
combo_unit = ttk.Combobox(window, width=35, textvariable=n)
combo_unit.place(relx=0.55, rely=0.28, anchor='center')
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


# Creating 'From' Lable
label_from = tk.Label(window, text='From', bg='gray', fg='black')
label_from['font'] = font1
label_from.place(relx=0.18, rely=0.35)

# Creating 'From' Combobox
f = tk.StringVar()
combo_from = ttk.Combobox(window, width=35, textvariable=f)
combo_from.place(relx=0.55, rely=0.38, anchor='center')
combo_from.current()
combo_from.bind('<<ComboboxSelected>>', fromfunc)

# Creating From Entry box
entry_f = tk.StringVar()
entry_from = tk.Entry(window, width=10, textvariable=entry_f)
entry_from.place(relx=0.82, rely=0.36)


# Creating 'To' Lable
label_to = tk.Label(window, text='To', bg='gray', fg='black')
label_to['font'] = font1
label_to.place(relx=0.18, rely=0.45)

# Creating 'To' Combobox
t = tk.StringVar()
combo_to = ttk.Combobox(window, width=35, textvariable=t)
combo_to.place(relx=0.55, rely=0.48, anchor='center')
combo_to.current()
combo_to.bind('<<ComboboxSelected>>', tofunc)

# Creating Result_section Lable
label_result =tk.Label(window, text='', bg='white', width=20)
label_result['font'] = font2
label_result.place(relx=0.21, rely=0.6)

# Creating Convert Button
btn_convert = tk.Button(window, text='Convert', bg='Cyan1', command=convert)
btn_convert['font'] = font1
btn_convert.place(relx=0.51, rely=0.8, anchor='center')

# Creating MainLoop
window.mainloop()