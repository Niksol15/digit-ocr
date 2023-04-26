from tkinter import *

import numpy as np
import tensorflow as tf
from tensorflow import keras

size = 400
pixels = 28
pixel_per_size = size / pixels
utility_padding = 30

app = Tk()
app.geometry(f"{size}x{size}")
draw_place=Canvas(app, bg='black')
draw_place.pack(anchor='nw', fill='both', expand=1)
app.geometry(f"{size }x{size + utility_padding}")
reset_button = Button(app, text="Reset")
reset_button.pack(side=BOTTOM)
result_label = Label(app)
result_label.pack(side=BOTTOM)

image = np.zeros(shape=(pixels, pixels, 1))

model = keras.models.load_model('model')

def get_x_and_y(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y

def draw_smth(event):
    global lasx, lasy

    pos_x = int(lasx // pixel_per_size) % pixels
    x1 = pos_x * pixel_per_size
    x2 = (pos_x + 1) * pixel_per_size

    pos_y = int(lasy // pixel_per_size) % pixels
    y1 = pos_y * pixel_per_size
    y2 = (pos_y + 1) * pixel_per_size

    image[pos_y][pos_x][0] = 255

    draw_place.create_rectangle(x1, y1, x2, y2, fill='white')
    result = model.predict(np.array([image,]))
    result = np.argmax(result, axis=1)
    result_label.config(text=f'{result[0]}')

    lasx, lasy = event.x, event.y

def reset(event):
    global image, draw_place
    draw_place.delete('all')
    image = np.zeros(shape=(pixels, pixels, 1))
    result_label.config(text='')

draw_place.bind("<Button-1>", get_x_and_y)
draw_place.bind("<B1-Motion>", draw_smth)

reset_button.bind('<Button-1>', reset)
app.mainloop()

