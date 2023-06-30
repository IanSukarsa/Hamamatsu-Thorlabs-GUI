## Libraries
#Instruments
import logging
from hamamatsu.dcam import copy_frame, dcam, Stream
from instrumental.drivers.cameras import uc480
import cv2

#Plotting
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Miscellaneous
import numpy as np
import time
import math as ma

#Window
import tkinter as tk
from tkinter import *
from tkinter import ttk


## Functions



with dcam:
    camera = dcam[0]
    with camera:
        # Simple acquisition example
        nb_frames = 10
        camera["exposure_time"] = float(expotime)
        with Stream(camera, nb_frames) as stream:
                logging.info("start acquisition")
                camera.start()
                for i, frame_buffer in enumerate(stream):
                    frame = copy_frame(frame_buffer)
                    logging.info(f"acquired frame #%d/%d: %s", i+1, nb_frames, frame)
                logging.info("finished acquisition")

def grab_frame():
    for i, frame_buffer in enumerate(stream):
        frame = copy_frame(frame_buffer)
        logging.info(f"acquired frame #%d/%d: %s", i+1, nb_frames, frame)
    logging.info("finished acquisition")


## Start
def StartHamamatsu():
    global Infotext
    Infotext["text"]="Hamamatsu GUI"

    global fig
    global ax
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

def StartThorlabs():
    global Infotext
    Infotext["text"]="Thorlabs GUI"




root = tk.Tk()
root.geometry("500x100")
root.title("Global Camera GUI")
frm = ttk.Frame(root, padding=10)
frm.grid()
Infotext=Label(frm, text="Welcome !")
Infotext.grid(column=0, row=0)
Quit=Button(frm, text="Quit", command=root.destroy)


Start_Hamamatsu=Button(frm, text="Hamamatsu Camera", command=StartHamamatsu)
Start_Thorlabs=Button(frm, text="Thorlabs Camera", command=StartThorlabs)
Quit.grid(column=10, row=1)
Start_Hamamatsu.grid(column=0, row=1)
Start_Thorlabs.grid(column=1,row=1)


root.mainloop()