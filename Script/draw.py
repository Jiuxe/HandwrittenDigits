from tkinter import Canvas, Tk, Button, messagebox, filedialog, Scale, HORIZONTAL, ALL

line_x = 0
line_y = 0
color = 'black'

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

window = Tk("HandWrittenDigits")
window.config(height=500,width=500,bg="black")

window.rowconfigure(1)
window.columnconfigure(1)

canvas = Canvas(window, bg="white")
canvas.grid(row=0,columnspan=2)

canvas.bind('<Button-1>',line_xy)
canvas.bind('<B1-Motion>',line)

clearButton = Button(window, command=clear, text="Limpiar", bg='red')
clearButton.grid(row=1, column=0, sticky='ew')

window.mainloop()
