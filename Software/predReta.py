from tkinter import *
from time import sleep
import numpy as np
from numpy.linalg import inv

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
	lista.append((event.x,event.y))

def drop(event):
	global lastx
	lastx = -1
	

def closing(event):
	global lista, lastx
	dados = np.array(lista)
	dados_x = dados[:, 0]
	dados_y = dados[:, 1]
	temp = []
	for i in range(0, dados_x.shape[0]):
		temp.append(1)

	A = np.column_stack((dados_x,np.array(temp)))
	y = dados_y.transpose()
	A_t = A.transpose()

	reduzida = np.dot(A_t, A)
	inv_reduzida = inv(reduzida)

	x = np.dot(np.dot(inv_reduzida, A_t), y)
	coef_ang = x[0]
	coef_lin = x[1]

	x_min = x_max = dados_x[0]
	for i in dados_x:
		x_min = min(x_min, i)
		x_max = max(x_max, i)
	w.create_line(x_min, coef_ang*x_min+coef_lin, x_max, coef_ang*x_max+coef_lin, fill="red", width="3")
	lista = []
	lastx = -1


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
