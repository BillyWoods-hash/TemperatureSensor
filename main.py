from random import randint
import tkinter as tk

# --- functions ---

last_values = []


def tempprobe():
    tempsimraw = randint(14, 30)  # Temperature simulation between 14 and 30
    last_values.append(tempsimraw)

    if len(last_values) == 4:
        tempsimsum = sum(last_values)
        temperature.set(tempsimsum / 4)

        last_values.clear()  # remove all values

        if tempsimsum / 4 > 25: # changes text colour to red if above temperature
            label_temperature.config(fg='red')
        else:  # changes text colour to black if not above temperature
            label_temperature.config(fg='Black')

        temperature_window.after(500, tempprobe)
    else:
        temperature_window.after(250, tempprobe)


# --- main ---

temperature_window = tk.Tk()

temperature = tk.DoubleVar(temperature_window)

label_temperature = tk.Label(temperature_window, textvariable=temperature)
label_temperature.pack()

button_start = tk.Button(temperature_window, text='Start', command=tempprobe)
button_start.pack()

temperature_window.mainloop()
