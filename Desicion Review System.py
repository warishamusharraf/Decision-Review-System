import cv2
import tkinter
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import time
import imutils
flag=True

# Creating Button play funtion
def play(speed):
    global flag
    print(f"you are clicking on button and speed is {speed}")
    stream=cv2.VideoCapture("runout.mp4")

    #play the video in reverse/backword mode
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)

    grabbed,frame=stream.read()
    frame=imutils.resize(frame,width=window_width,height=window_height)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    if flag:
        canvas.create_text(134,26,fill="black",font="Times 26 bold ",text="Decision Pending ")
    flag=not flag

    if not grabbed:
        exit()



def pending(desicion):
    # 1.display desicion pending image
    frame = cv2.cvtColor(cv2.imread("Decision Pending.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=window_width, height=window_height)
    frame = PIL.ImageTk.PhotoImage(PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 2.wait for 1  second
    time.sleep(5)

    # 3.display spnoser image
    frame = cv2.cvtColor(cv2.imread("sponser.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=window_width, height=window_height)
    frame = PIL.ImageTk.PhotoImage(PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 4 wait for 1.5 Seconds
    time.sleep(5.5)

    # 5 Display out/notOut Desicion
    if desicion=="Out":
        desicionImg="out.jpg"
    else:
        desicionImg="Not out.jpg"
    frame = cv2.cvtColor(cv2.imread(desicionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=window_width, height=window_height)
    frame = PIL.ImageTk.PhotoImage(PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 6 Wait for second 1.5
    time.sleep(2)


def Out():
    thread = threading.Thread(target=pending, args=("Out",))
    thread.daemon = 1
    thread.start()

def Not_Out():
    thread = threading.Thread(target=pending, args=("NotOut",))
    thread.daemon = 1
    thread.start()
    print("player is not out ")


# Window Width/Height Setting
window_width = 650
window_height = 368

# Main tkinter Screen Start!
window = tkinter.Tk()
window.title("Warisha Desicion Review System Kit")
cv_img = cv2.cvtColor(cv2.imread("Wel.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=window_width, height=window_height)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
create_canvas = (canvas.create_image(0, 0, ancho=tkinter.NW, image=photo))
canvas.pack()

# Button To Control Playback)
btn = tkinter.Button(window, text="<<Previous (fast)", width=50, command=partial(play, -25))
btn.pack()
btn = tkinter.Button(window, text="<<Previous (slow)", width=50, command=partial(play, -2))
btn.pack()
btn = tkinter.Button(window, text="Next     (fast)>>", width=50, command=partial(play, 25))
btn.pack()
btn = tkinter.Button(window, text="Next     (slow)>>", width=50, command=partial(play, 2))
btn.pack()
btn = tkinter.Button(window, text="Give Out", width=50, command=Out)
btn.pack()
btn = tkinter.Button(window, text="Give Not Out", width=50, command=Not_Out)
btn.pack()

window.mainloop()
