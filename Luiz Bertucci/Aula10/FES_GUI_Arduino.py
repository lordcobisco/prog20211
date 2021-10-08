import serial
import time
import tkinter
from scipy import signal 
import matplotlib.pyplot as plot 
import numpy as np 



def quit():
    global tkTop
    ser.write(bytes('Q', 'UTF-8'))
    tkTop.destroy()

#Liga estimulação alternada
def set_button1_state():
        varLabel.set("Monofásico ON  %s mA" %amplitude.get())
        ser.write(bytes('M', 'UTF-8'))
                
#Desliga estimulação alternada
def set_button2_state():
        varLabel.set("Estimulação - OFF")
        ser.write(bytes('O', 'UTF-8'))
#Liga estimulação mono
def set_button3_state():
        varLabel.set("Alternada ON  %s mA" %amplitude.get())
        ser.write(bytes('A', 'UTF-8'))
#Desliga estmulação monofásica
def set_button4_state():
        varLabel.set("Estimulação - 0FF")
        ser.write(bytes('O', 'UTF-8'))
#Gráfico Mono
def set_button5_state():
        t = np.linspace(0, 1, 1000, endpoint=True)  
        plot.plot(0.015+ t, 0.5 + (0.5 * signal.square(2 * np.pi * 10 * t)))
        plot.xlabel('Time') 
        plot.ylabel('Amplitude') 
        plot.title('Estimulação Alternada ')     
        plot.axhline(y = 0, color = 'k') 
        plot.show()
#Gráfico Alternada
def set_button6_state():
        t = np.linspace(0, 1, 1000, endpoint=True)  
        plot.plot(t, signal.square(2 * np.pi * 10 * t)) 
        plot.xlabel('Time') 
        plot.ylabel('Amplitude') 
        plot.title('Estimulação Mono')     
        plot.axhline(y = 0, color = 'k') 
        plot.show()

ser = serial.Serial('com3', 9600)
print("Reset Arduino")
time.sleep(3)
#ser.write(bytes('L', 'UTF-8'))

tkTop = tkinter.Tk()
tkTop.geometry('400x750')
tkTop.title("FES-INNELS")
label3 = tkinter.Label(text = 'Controlador FES',font=("Nunito", 9,'bold')).pack()
                      

varLabel = tkinter.IntVar()
tkLabel = tkinter.Label(textvariable=varLabel, )
tkLabel.pack()

label=tkinter.Label(tkTop, text="Corrente de Estimulação", bd = 4 ).pack()
amplitude = tkinter.Entry(tkTop)
amplitude.pack()


'''
varLabel2 = tkinter.IntVar()
tkLabel2 = tkinter.Label(textvariable=varLabel2, )
tkLabel2.pack()
'''
button1 = tkinter.IntVar()
button1state = tkinter.Button(tkTop,
    text="Start Monofásico",
    command=set_button1_state,
    height = 3,
    fg = "black",
    width = 12,
    bd = 4,
    activebackground='green'
)
button1state.pack(side='top', ipadx=10, padx=10, pady=15)

button2 = tkinter.IntVar()
button2state = tkinter.Button(tkTop,
    text="Stop Monofásico",
    command=set_button2_state,
    height = 3,
    fg = "black",
    width = 12,
    bd = 4,
    activebackground='red'
)
button2state.pack(side='top', ipadx=10, padx=10, pady=15)

button3 = tkinter.IntVar()
button3state = tkinter.Button(tkTop,
    text="Start Alternada",
    command=set_button3_state,
    height = 3,
    fg = "black",
    width = 12,
    bd = 3,
    activebackground='green'
)
button3state.pack(side='top', ipadx=10, padx=10, pady=15)

button4 = tkinter.IntVar()
button4state = tkinter.Button(tkTop,
    text="Stop Alternada",
    command=set_button4_state,
    height = 3,
    fg = "black",
    width = 12,
    bd = 4,
    activebackground='red'
)
button4state.pack(side='top', ipadx=10, padx=10, pady=15)

button5 = tkinter.IntVar()
button5state = tkinter.Button(tkTop,
    text="Gráfico Mono",
    command=set_button5_state,
    height = 3,
    fg = "black",
    width = 12,
    bd = 4,
    activebackground='purple'
)
button5state.pack(side='top', ipadx=10, padx=10, pady=15)

button6 = tkinter.IntVar()
button6state = tkinter.Button(tkTop,
    text="Gráfico Alternada",
    command=set_button6_state,
    height = 3,
    fg = "black",
    width = 12,
    bd = 4,
    activebackground='purple'
)
button6state.pack(side='top', ipadx=10, padx=10, pady=15)

tkButtonQuit = tkinter.Button(
    tkTop,
    text="Quit",
    command=quit,
    height = 4,
    fg = "black",
    width = 8,
    activebackground = 'yellow',
    bd = 5
)
tkButtonQuit.pack(side='top', ipadx=10, padx=10, pady=15)

tkinter.mainloop()