from tkinter import Canvas, Tk, Button, messagebox, filedialog, Scale, HORIZONTAL, ALL
import PIL.ImageGrab as ImageGrab
import numpy as np
import matplotlib.pyplot as plt
import main

line_x = 0
line_y = 0
color = 'white'

def line_xy(event):
    global line_x, line_y
    line_x = event.x
    line_y = event.y

def line(event):
    global line_x, line_y
    canvas.create_line((line_x,line_y, event.x, event.y), fill=color, width=10)
    line_x = event.x
    line_y = event.y

def clear():
    canvas.delete(ALL)

def quit():
    window.destroy()
    window.quit()

def getDraw():
    x = window.winfo_rootx() + canvas.winfo_x()
    y = window.winfo_rooty() + canvas.winfo_y()

    canvas_x = x + canvas.winfo_width()
    canvas_y = y + canvas.winfo_height()

    image = ImageGrab.grab().crop((x+2,y+2,canvas_x-2,canvas_y-2))
    image = image.convert('L')
    image = image.resize((28,28))

    imageArray = np.array(image)

    return imageArray

def trainingModel():
    print("Comienza entrenamiento")
    main.trainingModel()
    print("Termina entrenamiento")

def drawAnalysis():
    image = getDraw()
    print(main.evaluateOneElement(image))

window = Tk("HandWrittenDigits")
window.config(height=500,width=500,bg="black")

window.rowconfigure(1)
window.columnconfigure(2)

canvas = Canvas(window, bg="black")
canvas.grid(row=0,columnspan=3)

canvas.bind('<Button-1>',line_xy)
canvas.bind('<B1-Motion>',line)

clearButton = Button(window, command=clear, text="Limpiar", bg='red')
clearButton.grid(row=1, column=0, sticky='ew')

analysisButton = Button(window, command=drawAnalysis, text="Analizar dibujo", bg='green')
analysisButton.grid(row=1, column=1, sticky='ew')

trainingButton = Button(window, command=trainingModel, text="Entrenar Modelo", bg='blue')
trainingButton.grid(row=1, column=2, sticky='ew')

window.mainloop()
