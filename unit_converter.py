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
def convert(n1):
    num1 = n1.get()
    try:
        number1 = int(num1)
    except:
        messagebox.showerror('Error','Term not recognised')
    ## Digital Storage
    # Byte to other
    if result_from == 'Byte' and result_to == 'Byte':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'Byte'))
    elif result_from == 'Byte' and result_to == 'KiloByte':
        calculate = number1*0.0009765625
        label_result.cget('text')
        label_result.configure(text = (calculate, 'KB'))
    elif result_from == 'Byte' and result_to == 'MegaByte':
        calculate = number1*1048576
        label_result.cget('text')
        label_result.configure(text = (calculate, 'MB'))
    elif result_from == 'Byte' and result_to == 'GigaByte':
        calculate = number1*1073741824
        label_result.cget('text')
        label_result.configure(text = (calculate, 'GB'))
    elif result_from == 'Byte' and result_to == 'TeraByte':
        calculate = number1*1099511627776
        label_result.cget('text')
        label_result.configure(text = (calculate, 'TB'))
    elif result_from == 'Byte' and result_to == 'PetaByte':
        calculate = number1*1125899906842624
        label_result.cget('text')
        label_result.configure(text = (calculate, 'PB'))
    # KiloByte to other
    elif result_from == 'KiloByte' and result_to == 'Byte':
        calculate = number1*1024
        label_result.cget('text')
        label_result.configure(text = (calculate, 'Byte'))
    elif result_from == 'KiloByte' and result_to == 'KiloByte':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'KB'))
    elif result_from == 'KiloByte' and result_to == 'MegaByte':
        calculate = number1*0.0009765625
        label_result.cget('text')
        label_result.configure(text = (calculate, 'MB'))
    elif result_from == 'KiloByte' and result_to == 'GigaByte':
        calculate = number1*1048576
        label_result.cget('text')
        label_result.configure(text = (calculate, 'GB'))
    elif result_from == 'KiloByte' and result_to == 'TeraByte':
        calculate = number1*1073741824
        label_result.cget('text')
        label_result.configure(text = (calculate, result_to))
    elif result_from == 'KiloByte' and result_to == 'PetaByte':
        calculate = number1*1099511627776
        label_result.cget('text')
        label_result.configure(text = (calculate, 'PB'))
    # MegaByte to other
    elif result_from == 'MegaByte' and result_to == 'Byte':
        calculate = number1*1048576
        label_result.cget('text')
        label_result.configure(text = (calculate, 'Byte'))
    elif result_from == 'MegaByte' and result_to == 'KiloByte':
        calculate = number1*1024
        label_result.cget('text')
        label_result.configure(text = (calculate, 'KB'))
    elif result_from == 'MegaByte' and result_to == 'MegaByte':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'MB'))
    elif result_from == 'MegaByte' and result_to == 'GigaByte':
        calculate = number1*0.0009765625
        label_result.cget('text')
        label_result.configure(text = (calculate, 'GB'))
    elif result_from == 'MegaByte' and result_to == 'TeraByte':
        calculate = number1*1048576
        label_result.cget('text')
        label_result.configure(text = (calculate, 'TB'))
    elif result_from == 'MegaByte' and result_to == 'PetaByte':
        calculate = number1*1073741824
        label_result.cget('text')
        label_result.configure(text = (calculate, 'PB'))
    # GigaByte to other
    elif result_from == 'GigaByte' and result_to == 'Byte':
        calculate = number1*1073741824
        label_result.cget('text')
        label_result.configure(text = (calculate, result_to))
    elif result_from == 'GigaByte' and result_to == 'KiloByte':
        calculate = number1*1048576
        label_result.cget('text')
        label_result.configure(text = (calculate, 'KB'))
    elif result_from == 'GigaByte' and result_to == 'MegaByte':
        calculate = number1*1024
        label_result.cget('text')
        label_result.configure(text = (calculate, 'MB'))
    elif result_from == 'GigaByte' and result_to == 'GigaByte':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'GB'))
    elif result_from == 'GigaByte' and result_to == 'TeraByte':
        calculate = number1*0.0009765625
        label_result.cget('text')
        label_result.configure(text = (calculate, 'TB'))
    elif result_from == 'GigaByte' and result_to == 'PetaByte':
        calculate = number1*1048576
        label_result.cget('text')
        label_result.configure(text = (calculate, 'PB'))
    # TeraByte to other
    elif result_from == 'TeraByte' and result_to == 'Byte':
        calculate = number1*1099511627776
        label_result.cget('text')
        label_result.configure(text = (calculate, result_to))
    elif result_from == 'TeraByte' and result_to == 'KiloByte':
        calculate = number1*1073741824
        label_result.cget('text')
        label_result.configure(text = (calculate, 'KB'))
    elif result_from == 'TeraByte' and result_to == 'MegaByte':
        calculate = number1*1048576
        label_result.cget('text')
        label_result.configure(text = (calculate, 'MB'))
    elif result_from == 'TeraByte' and result_to == 'GigaByte':
        calculate = number1*1024
        label_result.cget('text')
        label_result.configure(text = (calculate, 'GB'))
    elif result_from == 'TeraByte' and result_to == 'TeraByte':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'TB'))
    elif result_from == 'TeraByte' and result_to == 'PetaByte':
        calculate = number1*0.0009765625
        label_result.cget('text')
        label_result.configure(text = (calculate, 'PB'))
    # PetaByte to other
    elif result_from == 'PetaByte' and result_to == 'Byte':
        calculate = number1*1125899906842624
        label_result.cget('text')
        label_result.configure(text = (calculate, result_to))
    elif result_from == 'TPetaByte' and result_to == 'KiloByte':
        calculate = number1*1099511627776
        label_result.cget('text')
        label_result.configure(text = (calculate, 'KB'))
    elif result_from == 'PetaByte' and result_to == 'MegaByte':
        calculate = number1*1073741824
        label_result.cget('text')
        label_result.configure(text = (calculate, 'MB'))
    elif result_from == 'PetaByte' and result_to == 'GigaByte':
        calculate = number1*1048576
        label_result.cget('text')
        label_result.configure(text = (calculate, 'GB'))
    elif result_from == 'PetaByte' and result_to == 'TeraByte':
        calculate = number1*1024
        label_result.cget('text')
        label_result.configure(text = (calculate, 'TB'))
    elif result_from == 'PetaByte' and result_to == 'PetaByte':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, result_to))

# Selected Function
def selected(event):
    unit = event.widget.get()
    if unit == 'Digital Storage':
        combo_from['values'] = ('Byte',
                                'KiloByte',
                                'MegaByte',
                                'GigaByte',
                                'TeraByte',
                                'PetaByte')
        combo_to['values'] = ('Byte',
                              'KiloByte',
                              'MegaByte',
                              'GigaByte',
                              'TeraByte',
                              'PetaByte')
    elif unit == 'Frequency':
        combo_from['values'] = ('Hertz',
                                'Kilohertz',
                                'Megahertz',
                                'Gigahertz')
        combo_to['values'] = ('Hertz',
                              'Kilohertz',
                              'Megahertz',
                              'Gigahertz')
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
        combo_from['values'] = ('Miles per Hour',
                                'Foot per Second',
                                'Meter per Second',
                                'Kilometer per Hour',
                                'Knot')
        combo_to['values'] = ('Miles per Hour',
                              'Foot per Second',
                              'Meter per Second',
                              'Kilometer per Hour',
                              'Knot')
    elif unit == 'Temperature':
        combo_from['values'] = ('Celsius',
                                'Fahrenheit',
                                'Kelvin')
        combo_to['values'] = ('Celsius',
                              'Fahrenheit',
                              'Kelvin')
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
        combo_from['values'] = ('Nanosecond',
                                'Microsecond',
                                'Millisecond',
                                'Second',
                                'Minute',
                                'Hour',
                                'Day',
                                'Week',
                                'Month',
                                'Year',
                                'Decade',
                                'Century')
        combo_to['values'] = ('Nanosecond',
                              'Microsecond',
                              'Millisecond',
                              'Second',
                              'Minute',
                              'Hour',
                              'Day',
                              'Week',
                              'Month',
                              'Year',
                              'Decade',
                              'Century')
    else:
        pass

# From Function
def fromfunc(event):
    global result_from
    result_from = event.widget.get()

# To Function
def tofunc(event):
    global result_to
    result_to = event.widget.get()

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
combo_unit['values'] = ('Digital Storage',
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
convert = partial(convert, entry_f)

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