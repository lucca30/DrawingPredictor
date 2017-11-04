from tkinter import *
from time import sleep
import numpy as np
"""
def circle(canvas,x,y, r):
   canvas.create_oval(x-r,y-r,x+r,y+r)
   return id

def bola(x, y):
	circle(w, x, y, 0)
	circle(w, x, y, 1)
	circle(w, x, y, 2)
"""
def drawing(event):
	global lastx, lasty
	if(lastx!=-1):
		w.create_line(lastx, lasty, event.x, event.y, fill="black", width="2")
	lastx,lasty = event.x,event.y
	lista.append((event.x, event.y))

def drop(event):
	global lastx
	lastx = -1

def closing(event):
	print("Terminando a aplicação de coleção de pontos, favor informar o nome de saída do arquivo (formato .npy)")
	string = input()
	np.save(string, np.array(lista))


master = Tk()
lastx = -1
lasty = -1
lista = []
canvas_width = 800
canvas_height = 600
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)

w.configure(cursor="crosshair")

w.bind("<Button-1>", drawing)
w.bind("<B1-Motion>", drawing)
w.bind("<ButtonRelease-1>", drop)

w.focus_set()
w.bind("<Key>", closing)

w.pack()

mainloop()
