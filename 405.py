'''
Created on Apr 2, 2019

@author: s271486
'''

from tkinter import *

root = Tk()

root.title("Volume of a cylinder")
root.geometry("200x400")


def calculation(r, h):
    volume = (3.14 * r**2)*h
    return volume

def radius():
    user_radius = int(radiusbox.get())
    return user_radius
    
def height():
    user_radius = int(heightbox.get())
    return user_radius

def output(ans):
    ans= Label(root, text=ans) 
    ans.pack()

radiuslab=Label(root, text= "Enter the radius of your cylinder")
radiuslab.pack()

radiusbox = Entry(root)
radiusbox.pack()
    
    
heightlab=Label(root, text= "Enter the height of your cylinder")
heightlab.pack()

heightbox = Entry(root)
heightbox.pack()

Button1 = Button(root, text= "Calculate" , command= lambda: output(calculation(radius(), height())))
Button1.pack()

root.mainloop()


