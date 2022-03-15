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
window.configure(bg = 'cyan2')

#Changing icon
icon = tk.PhotoImage(file='C:/Users/Pika pie/Pictures/Saved Pictures/Logo.png')
window.iconphoto(True, icon)

# Creating the Fonts
font_head = font.Font(family='helvetica', size='25')
font1 = font.Font(family='Ariel', size='15')
font2 = font.Font(family='Comic Sans', size='20')

# [All Functions]
# Convert Function
def convert(n1):
    num1 = n1.get()
    try:
        number1 = float(num1)
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
        label_result.configure(text = (calculate, 'TB'))
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
        label_result.configure(text = (calculate, 'PB'))

    ## Frequency
    # Hertz to other
    elif result_from == 'Hertz' and result_to == 'Hertz':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'Hz'))
    elif result_from == 'Hertz' and result_to == 'Kilohertz':
        calculate = number1/1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'kHz'))
    elif result_from == 'Hertz' and result_to == 'Megahertz':
        calculate = number1/1000000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'MHz'))
    elif result_from == 'Hertz' and result_to == 'Gigahertz':
        calculate = number1/1000000000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'GHz'))
    # Kilohertz to other
    elif result_from == 'Kilohertz' and result_to == 'Hertz':
        calculate = number1*1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'Hz'))
    elif result_from == 'Kilohertz' and result_to == 'Kilohertz':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'kHz'))
    elif result_from == 'Kilohertz' and result_to == 'Megahertz':
        calculate = number1/1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'MHz'))
    elif result_from == 'Kilohertz' and result_to == 'Gigahertz':
        calculate = number1/1000000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'GHz'))
    # Megahertz to other
    elif result_from == 'Megahertz' and result_to == 'Hertz':
        calculate = number1*1000000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'Hz'))
    elif result_from == 'Megahertz' and result_to == 'Kilohertz':
        calculate = number1*1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'kHz'))
    elif result_from == 'Megahertz' and result_to == 'Megahertz':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'MHz'))
    elif result_from == 'Megahertz' and result_to == 'Gigahertz':
        calculate = number1/1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'GHz'))
    # Gigahertz to other
    elif result_from == 'Gigahertz' and result_to == 'Hertz':
        calculate = number1*1000000000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'Hz'))
    elif result_from == 'Gigahertz' and result_to == 'Kilohertz':
        calculate = number1*1000000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'kHz'))
    elif result_from == 'Gigahertz' and result_to == 'Megahertz':
        calculate = number1*1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'MHz'))
    elif result_from == 'Gigahertz' and result_to == 'Gigahertz':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'GHz'))

    ## Length
    # Millimeter to other
    elif result_from == 'Millimeter' and result_to == 'Millimeter':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'mm'))
    elif result_from == 'Millimeter' and result_to == 'Centimeter':
        calculate = number1/10
        label_result.cget('text')
        label_result.configure(text = (calculate, 'cm'))
    elif result_from == 'Millimeter' and result_to == 'Decimeter':
        calculate = number1/100
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dm'))
    elif result_from == 'Millimeter' and result_to == 'Meter':
        calculate = number1/1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'm'))
    elif result_from == 'Millimeter' and result_to == 'Kilometer':
        calculate = number1/1000000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'km'))
    # Centimeter to other
    elif result_from == 'Centimeter' and result_to == 'Millimeter':
        calculate = number1*10
        label_result.cget('text')
        label_result.configure(text = (calculate, 'mm'))
    elif result_from == 'Centimeter' and result_to == 'Centimeter':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'cm'))
    elif result_from == 'Centimeter' and result_to == 'Decimeter':
        calculate = number1/10
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dm'))
    elif result_from == 'Centimeter' and result_to == 'Meter':
        calculate = number1/100
        label_result.cget('text')
        label_result.configure(text = (calculate, 'm'))
    elif result_from == 'Centimeter' and result_to == 'Kilometer':
        calculate = number1/100000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'km'))
    # Decimeter to other
    elif result_from == 'Decimeter' and result_to == 'Millimeter':
        calculate = number1*100
        label_result.cget('text')
        label_result.configure(text = (calculate, 'mm'))
    elif result_from == 'Decimeter' and result_to == 'Centimeter':
        calculate = number1*10
        label_result.cget('text')
        label_result.configure(text = (calculate, 'cm'))
    elif result_from == 'Decimeter' and result_to == 'Decimeter':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dm'))
    elif result_from == 'Decimeter' and result_to == 'Meter':
        calculate = number1/10
        label_result.cget('text')
        label_result.configure(text = (calculate, 'm'))
    elif result_from == 'Decimeter' and result_to == 'Kilometer':
        calculate = number1/10000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'km'))
    # Meter to other
    elif result_from == 'Meter' and result_to == 'Millimeter':
        calculate = number1*1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'mm'))
    elif result_from == 'Meter' and result_to == 'Centimeter':
        calculate = number1*100
        label_result.cget('text')
        label_result.configure(text = (calculate, 'cm'))
    elif result_from == 'Meter' and result_to == 'Decimeter':
        calculate = number1*10
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dm'))
    elif result_from == 'Meter' and result_to == 'Meter':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'm'))
    elif result_from == 'Meter' and result_to == 'Kilometer':
        calculate = number1/1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'km'))
    # Kilometer to other
    elif result_from == 'Kilometer' and result_to == 'Millimeter':
        calculate = number1*1000000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'mm'))
    elif result_from == 'Kilometer' and result_to == 'Centimeter':
        calculate = number1*100000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'cm'))
    elif result_from == 'Kilometer' and result_to == 'Decimeter':
        calculate = number1*10000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dm'))
    elif result_from == 'Kilometer' and result_to == 'Meter':
        calculate = number1*1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'm'))
    elif result_from == 'Kilometer' and result_to == 'Kilometer':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'km'))

    ## Mass
    # Milligram to other
    elif result_from == 'Milligram' and result_to == 'Milligram':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'mg'))
    elif result_from == 'Milligram' and result_to == 'Centigram':
        calculate = number1/10
        label_result.cget('text')
        label_result.configure(text = (calculate, 'cg'))
    elif result_from == 'Milligram' and result_to == 'Gram':
        calculate = number1/1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'g(gm)'))
    elif result_from == 'Milligram' and result_to == 'Decigram':
        calculate = number1/100
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dg'))
    elif result_from == 'Milligram' and result_to == 'Kilogram':
        calculate = number1/1000000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'kg'))
    # Centigram to other
    elif result_from == 'Centigram' and result_to == 'Milligram':
        calculate = number1*10
        label_result.cget('text')
        label_result.configure(text = (calculate, 'mg'))
    elif result_from == 'Centigram' and result_to == 'Centigram':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'cg'))
    elif result_from == 'Centigram' and result_to == 'Gram':
        calculate = number1/100
        label_result.cget('text')
        label_result.configure(text = (calculate, 'g(gm)'))
    elif result_from == 'Centigram' and result_to == 'Decigram':
        calculate = number1/10
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dg'))
    elif result_from == 'Centigram' and result_to == 'Kilogram':
        calculate = number1/100000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'kg'))
    # Gram to other
    elif result_from == 'Gram' and result_to == 'Milligram':
        calculate = number1*1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'mg'))
    elif result_from == 'Gram' and result_to == 'Centigram':
        calculate = number1*100
        label_result.cget('text')
        label_result.configure(text = (calculate, 'cg'))
    elif result_from == 'Gram' and result_to == 'Gram':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'g(gm)'))
    elif result_from == 'Gram' and result_to == 'Decigram':
        calculate = number1*10
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dg'))
    elif result_from == 'Gram' and result_to == 'Kilogram':
        calculate = number1/1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'kg'))
    # Decigram to other
    elif result_from == 'Decigram' and result_to == 'Milligram':
        calculate = number1*100
        label_result.cget('text')
        label_result.configure(text = (calculate, 'mg'))
    elif result_from == 'Decigram' and result_to == 'Centigram':
        calculate = number1*10
        label_result.cget('text')
        label_result.configure(text = (calculate, 'cg'))
    elif result_from == 'Decigram' and result_to == 'Gram':
        calculate = number1/10
        label_result.cget('text')
        label_result.configure(text = (calculate, 'g(gm)'))
    elif result_from == 'Decigram' and result_to == 'Decigram':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dg'))
    elif result_from == 'Decigram' and result_to == 'Kilogram':
        calculate = number1/10000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'kg'))
    # Kilogram to other
    elif result_from == 'Kilogram' and result_to == 'Milligram':
        calculate = number1*1000000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'mg'))
    elif result_from == 'Kilogram' and result_to == 'Centigram':
        calculate = number1*100000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'cg'))
    elif result_from == 'Kilogram' and result_to == 'Gram':
        calculate = number1*1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'g(gm)'))
    elif result_from == 'Kilogram' and result_to == 'Decigram':
        calculate = number1*10000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dg'))
    elif result_from == 'Kilogram' and result_to == 'Kilogram':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'kg'))

    ## Speed
    # Miles per Hour to other
    elif result_from == 'Miles per Hour' and result_to == 'Miles per Hour':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'mph'))
    elif result_from == 'Miles per Hour' and result_to == 'Foot per Second':
        calculate = number1*1.46667
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ft/s'))
    elif result_from == 'Miles per Hour' and result_to == 'Meter per Second':
        calculate = number1/2.237
        label_result.cget('text')
        label_result.configure(text = (calculate, 'm/sec'))
    elif result_from == 'Miles per Hour' and result_to == 'Kilometer per Hour':
        calculate = number1*1.60934
        label_result.cget('text')
        label_result.configure(text = (calculate, 'km/h'))
    elif result_from == 'Miles per Hour' and result_to == 'Knot':
        calculate = number1/1.151
        label_result.cget('text')
        label_result.configure(text = (calculate, 'kn(kt)'))
    # Foot per Second to other
    elif result_from == 'Foot per Second' and result_to == 'Miles per Hour':
        calculate = number1/1.46667
        label_result.cget('text')
        label_result.configure(text = (calculate, 'mph'))
    elif result_from == 'Foot per Second' and result_to == 'Foot per Second':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ft/s'))
    elif result_from == 'Foot per Second' and result_to == 'Meter per Second':
        calculate = number1/3.281
        label_result.cget('text')
        label_result.configure(text = (calculate, 'm/sec'))
    elif result_from == 'Foot per Second' and result_to == 'Kilometer per Hour':
        calculate = number1*1.097
        label_result.cget('text')
        label_result.configure(text = (calculate, 'km/h'))
    elif result_from == 'Foot per Second' and result_to == 'Knot':
        calculate = number1/1.688
        label_result.cget('text')
        label_result.configure(text = (calculate, 'kn(kt)'))
    # Meter per Second to other
    elif result_from == 'Meter per Second' and result_to == 'Miles per Hour':
        calculate = number1*2.237
        label_result.cget('text')
        label_result.configure(text = (calculate, 'mph'))
    elif result_from == 'Meter per Second' and result_to == 'Foot per Second':
        calculate = number1*3.28084
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ft/s'))
    elif result_from == 'Meter per Second' and result_to == 'Meter per Second':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'm/sec'))
    elif result_from == 'Meter per Second' and result_to == 'Kilometer per Hour':
        calculate = number1*3.6
        label_result.cget('text')
        label_result.configure(text = (calculate, 'km/h'))
    elif result_from == 'Meter per Second' and result_to == 'Knot':
        calculate = number1*1.94384
        label_result.cget('text')
        label_result.configure(text = (calculate, 'kn(kt)'))
    # Kilometer per Hour to other
    elif result_from == 'Kilometer per Hour' and result_to == 'Miles per Hour':
        calculate = number1/1.609
        label_result.cget('text')
        label_result.configure(text = (calculate, 'mph'))
    elif result_from == 'Kilometer per Hour' and result_to == 'Foot per Second':
        calculate = number1/1.097
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ft/s'))
    elif result_from == 'Kilometer per Hour' and result_to == 'Meter per Second':
        calculate = number1/3.6
        label_result.cget('text')
        label_result.configure(text = (calculate, 'm/sec'))
    elif result_from == 'Kilometer per Hour' and result_to == 'Kilometer per Hour':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'km/h'))
    elif result_from == 'Kilometer per Hour' and result_to == 'Knot':
        calculate = number1/1.852
        label_result.cget('text')
        label_result.configure(text = (calculate, 'kn(kt)'))
    # Knot Hour to other
    elif result_from == 'Knot' and result_to == 'Miles per Hour':
        calculate = number1*1.15078
        label_result.cget('text')
        label_result.configure(text = (calculate, 'mph'))
    elif result_from == 'Knot' and result_to == 'Foot per Second':
        calculate = number1*1.68781
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ft/s'))
    elif result_from == 'Knot' and result_to == 'Meter per Second':
        calculate = number1/1.944
        label_result.cget('text')
        label_result.configure(text = (calculate, 'm/sec'))
    elif result_from == 'Knot' and result_to == 'Kilometer per Hour':
        calculate = number1*1.852
        label_result.cget('text')
        label_result.configure(text = (calculate, 'km/h'))
    elif result_from == 'Knot' and result_to == 'Knot':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'kn(kt)'))

    ## Temperature
    # Celsius to other
    elif result_from == 'Celsius' and result_to == 'Celsius':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, '°C'))
    elif result_from == 'Celsius' and result_to == 'Fahrenheit':
        calculate = (number1 * (9/5)) + 32
        label_result.cget('text')
        label_result.configure(text = (calculate, '°F'))
    elif result_from == 'Celsius' and result_to == 'Kelvin':
        calculate = number1 + 273.15
        label_result.cget('text')
        label_result.configure(text = (calculate, '°K'))
    # Fahrenheit to other
    elif result_from == 'Fahrenheit' and result_to == 'Celsius':
        calculate = (number1 - 32)*(5/9)
        label_result.cget('text')
        label_result.configure(text = (calculate, '°C'))
    elif result_from == 'Fahrenheit' and result_to == 'Fahrenheit':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, '°F'))
    elif result_from == 'Fahrenheit' and result_to == 'Kelvin':
        calculate = (number1 - 32)*(5/9) + 273.15
        label_result.cget('text')
        label_result.configure(text = (calculate, '°K'))
    # Kelvin to other
    elif result_from == 'Kelvin' and result_to == 'Celsius':
        calculate = number1 - 273.15
        label_result.cget('text')
        label_result.configure(text = (calculate, '°C'))
    elif result_from == 'Kelvin' and result_to == 'Fahrenheit':
        calculate = (number1 - 273.15)*(9/5) + 32
        label_result.cget('text')
        label_result.configure(text = (calculate, '°F'))
    elif result_from == 'Kelvin' and result_to == 'Kelvin':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, '°K'))

    ## Volume
    # Cubic Meter to other
    elif result_from == 'Cubic Meter' and result_to == 'Cubic Meter':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'm³(CBM)'))
    elif result_from == 'Cubic Meter' and result_to == 'Milliliter':
        calculate = number1*1000000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'mL'))
    elif result_from == 'Cubic Meter' and result_to == 'Liter':
        calculate = number1*1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'L(l)'))
    elif result_from == 'Cubic Meter' and result_to == 'Gallon':
        calculate = number1*264.172
        label_result.cget('text')
        label_result.configure(text = (calculate, 'gal'))
    elif result_from == 'Cubic Meter' and result_to == 'Cubic Centimeter':
        calculate = number1*1000000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'cm³(ccm/cc)'))
    # Milliliter to other
    elif result_from == 'Milliliter' and result_to == 'Cubic Meter':
        calculate = number1/1000000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'm³(CBM)'))
    elif result_from == 'Milliliter' and result_to == 'Milliliter':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'mL'))
    elif result_from == 'Milliliter' and result_to == 'Liter':
        calculate = number1/1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'L(l)'))
    elif result_from == 'Milliliter' and result_to == 'Gallon':
        calculate = number1/3785
        label_result.cget('text')
        label_result.configure(text = (calculate, 'gal'))
    elif result_from == 'Milliliter' and result_to == 'Cubic Centimeter':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'cm³(ccm/cc)'))
    # Liter to other
    elif result_from == 'Liter' and result_to == 'Cubic Meter':
        calculate = number1/1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'm³(CBM)'))
    elif result_from == 'Liter' and result_to == 'Milliliter':
        calculate = number1*1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'mL'))
    elif result_from == 'Liter' and result_to == 'Liter':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'L(l)'))
    elif result_from == 'Liter' and result_to == 'Gallon':
        calculate = number1/3.785
        label_result.cget('text')
        label_result.configure(text = (calculate, 'gal'))
    elif result_from == 'Liter' and result_to == 'Cubic Centimeter':
        calculate = number1*1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'cm³(ccm/cc)'))
    # Gallon to other
    elif result_from == 'Gallon' and result_to == 'Cubic Meter':
        calculate = number1/264
        label_result.cget('text')
        label_result.configure(text = (calculate, 'm³(CBM)'))
    elif result_from == 'Gallon' and result_to == 'Milliliter':
        calculate = number1*3785
        label_result.cget('text')
        label_result.configure(text = (calculate, 'mL'))
    elif result_from == 'Gallon' and result_to == 'Liter':
        calculate = number1*3.785
        label_result.cget('text')
        label_result.configure(text = (calculate, 'L(l)'))
    elif result_from == 'Gallon' and result_to == 'Gallon':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'gal'))
    elif result_from == 'Gallon' and result_to == 'Cubic Centimeter':
        calculate = number1*3785
        label_result.cget('text')
        label_result.configure(text = (calculate, 'cm³(ccm/cc)'))
    # Cubic Centimeter to other
    elif result_from == 'Cubic Centimeter' and result_to == 'Cubic Meter':
        calculate = number1/1000000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'm³(CBM)'))
    elif result_from == 'Cubic Centimeter' and result_to == 'Milliliter':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'mL'))
    elif result_from == 'Cubic Centimeter' and result_to == 'Liter':
        calculate = number1/1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'L(l)'))
    elif result_from == 'Cubic Centimeter' and result_to == 'Gallon':
        calculate = number1/3785
        label_result.cget('text')
        label_result.configure(text = (calculate, 'gal'))
    elif result_from == 'Cubic Centimeter' and result_to == 'Cubic Centimeter':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'cm³(ccm/cc)'))

    ## Time
    # Nanosecond to other
    elif result_from == 'Nanosecond' and result_to == 'Nanosecond':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ns(nsec)'))
    elif result_from == 'Nanosecond' and result_to == 'Microsecond':
        calculate = number1/1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'µs'))
    elif result_from == 'Nanosecond' and result_to == 'Millisecond':
        calculate = number1/1000000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ms'))
    elif result_from == 'Nanosecond' and result_to == 'Second':
        calculate = number1/1000000000
        label_result.cget('text')
        label_result.configure(text = (calculate, 's(sec)'))
    elif result_from == 'Nanosecond' and result_to == 'Minute':
        calculate = number1/60000000000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'min'))
    elif result_from == 'Nanosecond' and result_to == 'Hour':
        calculate = number1/36000000000000      #3.6e+12
        label_result.cget('text')
        label_result.configure(text = (calculate, 'h(hr)'))
    elif result_from == 'Nanosecond' and result_to == 'Day':
        calculate = number1/86400000000000      #8.64e+13
        label_result.cget('text')
        label_result.configure(text = (calculate, 'd'))
    elif result_from == 'Nanosecond' and result_to == 'Week':
        calculate = number1/604800000000000         #6.048e+14
        label_result.cget('text')
        label_result.configure(text = (calculate, 'week'))
    elif result_from == 'Nanosecond' and result_to == 'Month':
        calculate = number1/2628000000000000        #2.628e+15
        label_result.cget('text')
        label_result.configure(text = (calculate, 'month'))
    elif result_from == 'Nanosecond' and result_to == 'Year':
        calculate = number1/31540000000000000       #3.154e+16
        label_result.cget('text')
        label_result.configure(text = (calculate, 'a(y/yr)'))
    elif result_from == 'Nanosecond' and result_to == 'Decade':
        calculate = number1/315400000000000000      #3.154e+17
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dec'))
    elif result_from == 'Nanosecond' and result_to == 'Century':
        calculate = number1/3154000000000000000         #3.154e+18
        label_result.cget('text')
        label_result.configure(text = (calculate, 'century'))
    # Microsecond to other
    elif result_from == 'Microsecond' and result_to == 'Nanosecond':
        calculate = number1*1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ns(nsec)'))
    elif result_from == 'Microsecond' and result_to == 'Microsecond':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'µs'))
    elif result_from == 'Microsecond' and result_to == 'Millisecond':
        calculate = number1/1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ms'))
    elif result_from == 'Microsecond' and result_to == 'Second':
        calculate = number1/1000000
        label_result.cget('text')
        label_result.configure(text = (calculate, 's(sec)'))
    elif result_from == 'Microsecond' and result_to == 'Minute':
        calculate = number1/(6*(10**7))         #6e+7
        label_result.cget('text')
        label_result.configure(text = (calculate, 'min'))
    elif result_from == 'Microsecond' and result_to == 'Hour':
        calculate = number1/(3.6*(10**9))       #3.6e+9
        label_result.cget('text')
        label_result.configure(text = (calculate, 'h(hr)'))
    elif result_from == 'Microsecond' and result_to == 'Day':
        calculate = number1/(8.64*(10**10))         #8.64e+10
        label_result.cget('text')
        label_result.configure(text = (calculate, 'd'))
    elif result_from == 'Microsecond' and result_to == 'Week':
        calculate = number1/(6.048*(10**11))        #6.048e+11
        label_result.cget('text')
        label_result.configure(text = (calculate, 'week'))
    elif result_from == 'Microsecond' and result_to == 'Month':
        calculate = number1/(2.628*(10**12))        #2.628e+12
        label_result.cget('text')
        label_result.configure(text = (calculate, 'month'))
    elif result_from == 'Microsecond' and result_to == 'Year':
        calculate = number1/(3.154*(10**13))        #3.154e+13
        label_result.cget('text')
        label_result.configure(text = (calculate, 'a(y/yr)'))
    elif result_from == 'Microsecond' and result_to == 'Decade':
        calculate = number1/(3.154*(10**14))        #3.154e+14
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dec'))
    elif result_from == 'Microsecond' and result_to == 'Century':
        calculate = number1/(3.154*(10**15))        #3.154e+15
        label_result.cget('text')
        label_result.configure(text = (calculate, 'century'))
    # Millisecond to other
    elif result_from == 'Millisecond' and result_to == 'Nanosecond':
        calculate = number1*(1*(10**6))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ns(nsec)'))
    elif result_from == 'Millisecond' and result_to == 'Microsecond':
        calculate = number1*1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'µs'))
    elif result_from == 'Millisecond' and result_to == 'Millisecond':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ms'))
    elif result_from == 'Millisecond' and result_to == 'Second':
        calculate = number1/1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 's(sec)'))
    elif result_from == 'Millisecond' and result_to == 'Minute':
        calculate = number1/60000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'min'))
    elif result_from == 'Millisecond' and result_to == 'Hour':
        calculate = number1/(3.6*(10**6))       #3.6e+6
        label_result.cget('text')
        label_result.configure(text = (calculate, 'h(hr)'))
    elif result_from == 'Millisecond' and result_to == 'Day':
        calculate = number1/(8.64*(10**7))      #8.64e+7
        label_result.cget('text')
        label_result.configure(text = (calculate, 'd'))
    elif result_from == 'Millisecond' and result_to == 'Week':
        calculate = number1/(6.048*(10**8))     #6.048e+8
        label_result.cget('text')
        label_result.configure(text = (calculate, 'week'))
    elif result_from == 'Millisecond' and result_to == 'Month':
        calculate = number1/(2.628*(10**9))     #2.628e+9
        label_result.cget('text')
        label_result.configure(text = (calculate, 'month'))
    elif result_from == 'Millisecond' and result_to == 'Year':
        calculate = number1/(3.154*(10**10))        #3.154e+10
        label_result.cget('text')
        label_result.configure(text = (calculate, 'a(y/yr)'))
    elif result_from == 'Millisecond' and result_to == 'Decade':
        calculate = number1/(3.154*(10**11))        #3.154e+11
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dec'))
    elif result_from == 'Millisecond' and result_to == 'Century':
        calculate = number1/(3.154*(10**12))        #3.154e+12
        label_result.cget('text')
        label_result.configure(text = (calculate, 'century'))
    # Second to other
    elif result_from == 'Second' and result_to == 'Nanosecond':
        calculate = number1*(1*(10**9))     #1e+9
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ns(nsec)'))
    elif result_from == 'Second' and result_to == 'Microsecond':
        calculate = number1*(1*(10**6))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'µs'))
    elif result_from == 'Second' and result_to == 'Millisecond':
        calculate = number1*1000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ms'))
    elif result_from == 'Second' and result_to == 'Second':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 's(sec)'))
    elif result_from == 'Second' and result_to == 'Minute':
        calculate = number1/60
        label_result.cget('text')
        label_result.configure(text = (calculate, 'min'))
    elif result_from == 'Second' and result_to == 'Hour':
        calculate = number1/3600
        label_result.cget('text')
        label_result.configure(text = (calculate, 'h(hr)'))
    elif result_from == 'Second' and result_to == 'Day':
        calculate = number1/86400
        label_result.cget('text')
        label_result.configure(text = (calculate, 'd'))
    elif result_from == 'Second' and result_to == 'Week':
        calculate = number1/604800
        label_result.cget('text')
        label_result.configure(text = (calculate, 'week'))
    elif result_from == 'Second' and result_to == 'Month':
        calculate = number1/(2.628*(10**6))     #2.628e+6
        label_result.cget('text')
        label_result.configure(text = (calculate, 'month'))
    elif result_from == 'Second' and result_to == 'Year':
        calculate = number1/(3.154*(10**7))     #3.154e+7
        label_result.cget('text')
        label_result.configure(text = (calculate, 'a(y/yr)'))
    elif result_from == 'Second' and result_to == 'Decade':
        calculate = number1/(3.154*(10**8))     #3.154e+8
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dec'))
    elif result_from == 'Second' and result_to == 'Century':
        calculate = number1/(3.154*(10**9))     #3.154e+9
        label_result.cget('text')
        label_result.configure(text = (calculate, 'century'))
    # Minute to other
    elif result_from == 'Minute' and result_to == 'Nanosecond':
        calculate = number1*(6*(10**10))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ns(nsec)'))
    elif result_from == 'Minute' and result_to == 'Microsecond':
        calculate = number1*(6*(10**7))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'µs'))
    elif result_from == 'Minute' and result_to == 'Millisecond':
        calculate = number1*60000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ms'))
    elif result_from == 'Minute' and result_to == 'Second':
        calculate = number1*60
        label_result.cget('text')
        label_result.configure(text = (calculate, 's(sec)'))
    elif result_from == 'Minute' and result_to == 'Minute':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'min'))
    elif result_from == 'Minute' and result_to == 'Hour':
        calculate = number1/60
        label_result.cget('text')
        label_result.configure(text = (calculate, 'h(hr)'))
    elif result_from == 'Minute' and result_to == 'Day':
        calculate = number1/1440
        label_result.cget('text')
        label_result.configure(text = (calculate, 'd'))
    elif result_from == 'Minute' and result_to == 'Week':
        calculate = number1/10080
        label_result.cget('text')
        label_result.configure(text = (calculate, 'week'))
    elif result_from == 'Minute' and result_to == 'Month':
        calculate = number1/43800
        label_result.cget('text')
        label_result.configure(text = (calculate, 'month'))
    elif result_from == 'Minute' and result_to == 'Year':
        calculate = number1/525600
        label_result.cget('text')
        label_result.configure(text = (calculate, 'a(y/yr)'))
    elif result_from == 'Minute' and result_to == 'Decade':
        calculate = number1/(5.256*(10**6))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dec'))
    elif result_from == 'Minute' and result_to == 'Century':
        calculate = number1/(5.256*(10**7))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'century'))
    # Hour to other
    elif result_from == 'Hour' and result_to == 'Nanosecond':
        calculate = number1*(3.6*(10**12))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ns(nsec)'))
    elif result_from == 'Hour' and result_to == 'Microsecond':
        calculate = number1*(3.6*(10**9))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'µs'))
    elif result_from == 'Hour' and result_to == 'Millisecond':
        calculate = number1*(3.6*(10**6))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ms'))
    elif result_from == 'Hour' and result_to == 'Second':
        calculate = number1*3600
        label_result.cget('text')
        label_result.configure(text = (calculate, 's(sec)'))
    elif result_from == 'Hour' and result_to == 'Minute':
        calculate = number1*60
        label_result.cget('text')
        label_result.configure(text = (calculate, 'min'))
    elif result_from == 'Hour' and result_to == 'Hour':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'h(hr)'))
    elif result_from == 'Hour' and result_to == 'Day':
        calculate = number1/24
        label_result.cget('text')
        label_result.configure(text = (calculate, 'd'))
    elif result_from == 'Hour' and result_to == 'Week':
        calculate = number1/168
        label_result.cget('text')
        label_result.configure(text = (calculate, 'week'))
    elif result_from == 'Hour' and result_to == 'Month':
        calculate = number1/730
        label_result.cget('text')
        label_result.configure(text = (calculate, 'month'))
    elif result_from == 'Hour' and result_to == 'Year':
        calculate = number1/8760
        label_result.cget('text')
        label_result.configure(text = (calculate, 'a(y/yr)'))
    elif result_from == 'Hour' and result_to == 'Decade':
        calculate = number1/87600
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dec'))
    elif result_from == 'Hour' and result_to == 'Century':
        calculate = number1/876000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'century'))
    # Day to other
    elif result_from == 'Day' and result_to == 'Nanosecond':
        calculate = number1*(8.64*(10**13))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ns(nsec)'))
    elif result_from == 'Day' and result_to == 'Microsecond':
        calculate = number1*(8.64*(10**10))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'µs'))
    elif result_from == 'Day' and result_to == 'Millisecond':
        calculate = number1*(8.64*(10**7))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ms'))
    elif result_from == 'Day' and result_to == 'Second':
        calculate = number1*86400
        label_result.cget('text')
        label_result.configure(text = (calculate, 's(sec)'))
    elif result_from == 'Day' and result_to == 'Minute':
        calculate = number1*1440
        label_result.cget('text')
        label_result.configure(text = (calculate, 'min'))
    elif result_from == 'Day' and result_to == 'Hour':
        calculate = number1*24
        label_result.cget('text')
        label_result.configure(text = (calculate, 'h(hr)'))
    elif result_from == 'Day' and result_to == 'Day':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'd'))
    elif result_from == 'Day' and result_to == 'Week':
        calculate = number1/7
        label_result.cget('text')
        label_result.configure(text = (calculate, 'week'))
    elif result_from == 'Day' and result_to == 'Month':
        calculate = number1/30.417
        label_result.cget('text')
        label_result.configure(text = (calculate, 'month'))
    elif result_from == 'Day' and result_to == 'Year':
        calculate = number1/365
        label_result.cget('text')
        label_result.configure(text = (calculate, 'a(y/yr)'))
    elif result_from == 'Day' and result_to == 'Decade':
        calculate = number1/3650
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dec'))
    elif result_from == 'Day' and result_to == 'Century':
        calculate = number1/36500
        label_result.cget('text')
        label_result.configure(text = (calculate, 'century'))
    # Week to other
    elif result_from == 'Week' and result_to == 'Nanosecond':
        calculate = number1*(6.048*(10**14))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ns(nsec)'))
    elif result_from == 'Week' and result_to == 'Microsecond':
        calculate = number1*(6.048*(10**11))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'µs'))
    elif result_from == 'Week' and result_to == 'Millisecond':
        calculate = number1*(6.048*(10**8))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ms'))
    elif result_from == 'Week' and result_to == 'Second':
        calculate = number1*604800
        label_result.cget('text')
        label_result.configure(text = (calculate, 's(sec)'))
    elif result_from == 'Week' and result_to == 'Minute':
        calculate = number1*10080
        label_result.cget('text')
        label_result.configure(text = (calculate, 'min'))
    elif result_from == 'Week' and result_to == 'Hour':
        calculate = number1*168
        label_result.cget('text')
        label_result.configure(text = (calculate, 'h(hr)'))
    elif result_from == 'Week' and result_to == 'Day':
        calculate = number1*7
        label_result.cget('text')
        label_result.configure(text = (calculate, 'd'))
    elif result_from == 'Week' and result_to == 'Week':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'week'))
    elif result_from == 'Week' and result_to == 'Month':
        calculate = number1/4.345
        label_result.cget('text')
        label_result.configure(text = (calculate, 'month'))
    elif result_from == 'Week' and result_to == 'Year':
        calculate = number1/52.143
        label_result.cget('text')
        label_result.configure(text = (calculate, 'a(y/yr)'))
    elif result_from == 'Week' and result_to == 'Decade':
        calculate = number1/521.43
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dec'))
    elif result_from == 'Week' and result_to == 'Century':
        calculate = number1/5214.3
        label_result.cget('text')
        label_result.configure(text = (calculate, 'century'))
    # Month to other
    elif result_from == 'Month' and result_to == 'Nanosecond':
        calculate = number1*(2.628*(10**15))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ns(nsec)'))
    elif result_from == 'Month' and result_to == 'Microsecond':
        calculate = number1*(2.628*(10**12))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'µs'))
    elif result_from == 'Month' and result_to == 'Millisecond':
        calculate = number1*(2.628*(10**9))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ms'))
    elif result_from == 'Month' and result_to == 'Second':
        calculate = number1*(2.628*(10**6))
        label_result.cget('text')
        label_result.configure(text = (calculate, 's(sec)'))
    elif result_from == 'Month' and result_to == 'Minute':
        calculate = number1*43800
        label_result.cget('text')
        label_result.configure(text = (calculate, 'min'))
    elif result_from == 'Month' and result_to == 'Hour':
        calculate = number1*730.001
        label_result.cget('text')
        label_result.configure(text = (calculate, 'h(hr)'))
    elif result_from == 'Month' and result_to == 'Day':
        calculate = number1*30.4167
        label_result.cget('text')
        label_result.configure(text = (calculate, 'd'))
    elif result_from == 'Month' and result_to == 'Week':
        calculate = number1*4.34524
        label_result.cget('text')
        label_result.configure(text = (calculate, 'week'))
    elif result_from == 'Month' and result_to == 'Month':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'month'))
    elif result_from == 'Month' and result_to == 'Year':
        calculate = number1/12
        label_result.cget('text')
        label_result.configure(text = (calculate, 'a(y/yr)'))
    elif result_from == 'Month' and result_to == 'Decade':
        calculate = number1/120
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dec'))
    elif result_from == 'Month' and result_to == 'Century':
        calculate = number1/1200
        label_result.cget('text')
        label_result.configure(text = (calculate, 'century'))
    # Year to other
    elif result_from == 'Year' and result_to == 'Nanosecond':
        calculate = number1*(3.154*(10**16))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ns(nsec)'))
    elif result_from == 'Year' and result_to == 'Microsecond':
        calculate = number1*(3.154*(10**13))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'µs'))
    elif result_from == 'Year' and result_to == 'Millisecond':
        calculate = number1*(3.154*(10**10))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ms'))
    elif result_from == 'Year' and result_to == 'Second':
        calculate = number1*(3.154*(10**7))
        label_result.cget('text')
        label_result.configure(text = (calculate, 's(sec)'))
    elif result_from == 'Year' and result_to == 'Minute':
        calculate = number1*525600
        label_result.cget('text')
        label_result.configure(text = (calculate, 'min'))
    elif result_from == 'Year' and result_to == 'Hour':
        calculate = number1*8760
        label_result.cget('text')
        label_result.configure(text = (calculate, 'h(hr)'))
    elif result_from == 'Year' and result_to == 'Day':
        calculate = number1*365
        label_result.cget('text')
        label_result.configure(text = (calculate, 'd'))
    elif result_from == 'Year' and result_to == 'Week':
        calculate = number1*52.1429
        label_result.cget('text')
        label_result.configure(text = (calculate, 'week'))
    elif result_from == 'Year' and result_to == 'Month':
        calculate = number1*12
        label_result.cget('text')
        label_result.configure(text = (calculate, 'month'))
    elif result_from == 'Year' and result_to == 'Year':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'a(y/yr)'))
    elif result_from == 'Year' and result_to == 'Decade':
        calculate = number1/10
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dec'))
    elif result_from == 'Year' and result_to == 'Century':
        calculate = number1/100
        label_result.cget('text')
        label_result.configure(text = (calculate, 'century'))
    # Decade to other
    elif result_from == 'Decade' and result_to == 'Nanosecond':
        calculate = number1*(3.154*(10**17))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ns(nsec)'))
    elif result_from == 'Decade' and result_to == 'Microsecond':
        calculate = number1*(3.154*(10**14))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'µs'))
    elif result_from == 'Decade' and result_to == 'Millisecond':
        calculate = number1*(3.154*(10**11))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ms'))
    elif result_from == 'Decade' and result_to == 'Second':
        calculate = number1*(3.154*(10**8))
        label_result.cget('text')
        label_result.configure(text = (calculate, 's(sec)'))
    elif result_from == 'Decade' and result_to == 'Minute':
        calculate = number1*(5.256*(10**6))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'min'))
    elif result_from == 'Decade' and result_to == 'Hour':
        calculate = number1*87600
        label_result.cget('text')
        label_result.configure(text = (calculate, 'h(hr)'))
    elif result_from == 'Decade' and result_to == 'Day':
        calculate = number1*3650
        label_result.cget('text')
        label_result.configure(text = (calculate, 'd'))
    elif result_from == 'Decade' and result_to == 'Week':
        calculate = number1*521.429
        label_result.cget('text')
        label_result.configure(text = (calculate, 'week'))
    elif result_from == 'Decade' and result_to == 'Month':
        calculate = number1*120
        label_result.cget('text')
        label_result.configure(text = (calculate, 'month'))
    elif result_from == 'Decade' and result_to == 'Year':
        calculate = number1*10
        label_result.cget('text')
        label_result.configure(text = (calculate, 'a(y/yr)'))
    elif result_from == 'Decade' and result_to == 'Decade':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dec'))
    elif result_from == 'Decade' and result_to == 'Century':
        calculate = number1/10
        label_result.cget('text')
        label_result.configure(text = (calculate, 'century'))
    # Century to other
    elif result_from == 'Century' and result_to == 'Nanosecond':
        calculate = number1*(3.154*(10**18))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ns(nsec)'))
    elif result_from == 'Century' and result_to == 'Microsecond':
        calculate = number1*(3.154*(10**15))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'µs'))
    elif result_from == 'Century' and result_to == 'Millisecond':
        calculate = number1*(3.154*(10**12))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'ms'))
    elif result_from == 'Century' and result_to == 'Second':
        calculate = number1*(3.154*(10**9))
        label_result.cget('text')
        label_result.configure(text = (calculate, 's(sec)'))
    elif result_from == 'Century' and result_to == 'Minute':
        calculate = number1*(5.256*(10**7))
        label_result.cget('text')
        label_result.configure(text = (calculate, 'min'))
    elif result_from == 'Century' and result_to == 'Hour':
        calculate = number1*876000
        label_result.cget('text')
        label_result.configure(text = (calculate, 'h(hr)'))
    elif result_from == 'Century' and result_to == 'Day':
        calculate = number1*36500
        label_result.cget('text')
        label_result.configure(text = (calculate, 'd'))
    elif result_from == 'Century' and result_to == 'Week':
        calculate = number1*5214.29
        label_result.cget('text')
        label_result.configure(text = (calculate, 'week'))
    elif result_from == 'Century' and result_to == 'Month':
        calculate = number1*1200
        label_result.cget('text')
        label_result.configure(text = (calculate, 'month'))
    elif result_from == 'Century' and result_to == 'Year':
        calculate = number1*100
        label_result.cget('text')
        label_result.configure(text = (calculate, 'a(y/yr)'))
    elif result_from == 'Century' and result_to == 'Decade':
        calculate = number1*10
        label_result.cget('text')
        label_result.configure(text = (calculate, 'dec'))
    elif result_from == 'Century' and result_to == 'Century':
        calculate = number1
        label_result.cget('text')
        label_result.configure(text = (calculate, 'century'))
    else:
        label_result.cget('text')
        label_result.configure(text='Select the unit properly!')
        messagebox.showerror('Warning', 'Select the unit properly!')

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
        combo_from['values'] = ('Millimeter',
                                'Centimeter',
                                'Decimeter',
                                'Meter',
                                'Kilometer')
        combo_to['values'] = ('Millimeter',
                              'Centimeter',
                              'Decimeter',
                              'Meter',
                              'Kilometer')
    elif unit == 'Mass':
        combo_from['values'] = ('Milligram',
                                'Centigram',
                                'Gram',
                                'Decigram',
                                'Kilogram')
        combo_to['values'] = ('Milligram',
                              'Centigram',
                              'Gram',
                              'Decigram',
                              'Kilogram')
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
        combo_from['values'] = ('Cubic Meter',
                                'Milliliter',
                                'Liter',
                                'Gallon',
                                'Cubic Centimeter')
        combo_to['values'] = ('Cubic Meter',
                              'Milliliter',
                              'Liter',
                              'Gallon',
                              'Cubic Centimeter')
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
label_title = tk.Label(window,
                       text='UNIT CONVERTER',
                       bg='cyan2',
                       fg='darkblue')
label_title['font'] = font_head
label_title.place(relx='0.5', rely='0.1', anchor='center')

# Creating Unit Lable
label_unit = tk.Label(window, text='Unit', bg='cyan2', fg='black')
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
label_from = tk.Label(window, text='From', bg='cyan2', fg='black')
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
label_to = tk.Label(window, text='To', bg='cyan2', fg='black')
label_to['font'] = font1
label_to.place(relx=0.18, rely=0.45)

# Creating 'To' Combobox
t = tk.StringVar()
combo_to = ttk.Combobox(window, width=35, textvariable=t)
combo_to.place(relx=0.55, rely=0.48, anchor='center')
combo_to.current()
combo_to.bind('<<ComboboxSelected>>', tofunc)

# Creating Result_section Lable
label_result = tk.Label(window, text='', bg='white', width=28, relief=tk.GROOVE, bd=5)
label_result['font'] = font2
label_result.place(relx=0.045, rely=0.6)

# Creating Convert Button
btn_convert = tk.Button(window, text='Convert', bg='red', fg='white', relief=tk.RAISED, bd=5, activeforeground='white', activebackground='#00ff00',command=convert)
btn_convert['font'] = font1
btn_convert.place(relx=0.51, rely=0.8, anchor='center')

# Creating MainLoop
window.mainloop()