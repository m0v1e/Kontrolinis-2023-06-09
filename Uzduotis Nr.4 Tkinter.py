from tkinter import *

langas = Tk()

# langas.geometry("250x100")

celsius = 0
fahrenheit = 0

def celsius_to_fahrenheit():
    ivestis = int(laukas1.get())
    fahrenheit = round(((ivestis * 9 / 5) + 32), 1)
    degree_symbol = "\u00B0"
    uzrasas1.config(text=f'Result: {fahrenheit} {degree_symbol}F')
    return fahrenheit

def fahrenheit_to_celsius():
    ivestis = int(laukas1.get())
    celsius = round(((ivestis - 32) * 5/9), 1)
    degree_symbol = "\u00B0"
    uzrasas1.config(text=f'Result: {celsius} {degree_symbol}C')
    return celsius


laukas1 = Entry(langas)
mygtukas1 = Button(langas, text="Fahrenheit to Celsius", command=fahrenheit_to_celsius)
mygtukas2 = Button(langas, text="Celsius to Fahrenheit", command=celsius_to_fahrenheit)
uzrasas1 = Label(langas)
uzsaras2 = Label(langas, text='Iveskite temperatura ir spauskite norima konvertavima')




laukas1.grid(row=1, column=0, columnspan=2, sticky=EW)
mygtukas1.grid(row=2, column=0, sticky=W)
mygtukas2.grid(row=2, column=1, sticky=E)
uzrasas1.grid(row=3, columnspan=2)
uzsaras2.grid(row=0, columnspan=2)



langas.mainloop()

