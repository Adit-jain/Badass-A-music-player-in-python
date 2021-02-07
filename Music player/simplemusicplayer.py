from tkinter import *
import pyglet
from PIL import ImageTk,Image
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar

pyglet.font.add_file('Music player\CHILLER.ttf')


def musicurl():
    dd = filedialog.askopenfilename(filetypes=[("MP3 Files",'*.mp3'),("WAV Files","*.WAV")])
    audiotrack.set(dd)
    root.play_button['state'] = NORMAL
    root.pause_button['state'] = NORMAL
    root.stop_button['state'] = NORMAL

def playmusic():
    global music_started
    root.pause_button['state'] = NORMAL
    if music_started:
        mixer.music.unpause()
    else:
        music_started = True
        ad = audiotrack.get()
        mixer.music.load(ad)
        mixer.music.play()


def pausemusic():
    mixer.music.pause()

def setvolume(vol):
    con_vol = float(int(vol)/100)
    mixer.music.set_volume(con_vol)

def stopmusic():
    
    global music_started
    music_started = False
    root.pause_button['state'] = DISABLED
    mixer.music.stop()


def createwidgets():
    #Labels
    track_label = Label(root,text = "Select Audio track", background = "Black",foreground = "Red", font=("CHILLER",25,'italic bold'))
    track_label.grid(row = 0, column = 0,padx = (130,20),pady=20)
    

    #Entry box
    track_label_entry = Entry(root,font=("CHILLER",25),width = 35,background = "Black",foreground = "Red",bd =10,textvariable = audiotrack)
    track_label_entry.grid(row = 0,column = 1,padx = 20,pady =20)
    
    
    #Buttons
    browse_button = Button(root,text = "BROWSE",background = "Black",foreground = "red", width = 15, font=("CHILLER",20,'italic bold'),bd = 5, command = musicurl)
    browse_button.grid(row =0, column =2)

    root.play_button = Button(root,text = "PLAY",background = "Black",foreground = "red", width = 15,
     font=("CHILLER",20,'italic'),bd = 5,command = playmusic,state = DISABLED)
    root.play_button.grid(row =1, column =0,pady=(0,0),padx = (130,0))

    root.pause_button = Button(root,text = "PAUSE",background = "Black",foreground = "red", width = 15,
     font=("CHILLER",20,'italic'),bd = 5,command = pausemusic,state = DISABLED)
    root.pause_button.grid(row =2, column =0,pady=(0,0),padx = (130,0))

    root.stop_button = Button(root,text = "STOP",background = "Black",foreground = "red", width = 15,
     font=("CHILLER",20,'italic'),bd = 5,command = stopmusic,state = DISABLED)
    root.stop_button.grid(row =3, column =0,pady=(0,0),padx = (130,0))

    Volume_scale = Scale(root,from_ = 0, to = 100, orient = VERTICAL,background = "Black",foreground = "Red",bd=10,font=("CHILLER",20),length = 300,sliderlength = 30,label = "VOLUME",command = setvolume )
    Volume_scale.set(100)
    Volume_scale.grid(row =1,column= 2,pady=(30,0),rowspan=5)

    #Background
    
    #Load image
    image1 = Image.open('Music player\skull.jpg')
    image2 = Image.open('Music player\stain.png')
    #resize image
    resized_image1 = image1.resize((round(image1.size[0]*0.4), round(image1.size[1]*0.4)))
    resized_image2 = image2.resize((round(image2.size[0]*0.6), round(image2.size[1]*0.6)))
    #convert image
    bgimage = ImageTk.PhotoImage(resized_image1)
    bg2image = ImageTk.PhotoImage(resized_image2)
    #create label
    bglabel = Label(root,image = bgimage,background = "Black")
    bg2label = Label(root,image = bg2image,background = "Black")
    #assign image
    bglabel.image = bgimage
    bg2label.image = bg2image
    #place image
    bglabel.grid(row = 1,column = 1,rowspan =5,pady=(30,0))
    bg2label.grid(row=0,column = 1)
    track_label_entry.tkraise()

##########################################################################################
root = Tk()
root.geometry('1300x700+100+60')
root.title("Badass music")
root.iconbitmap('Music player\Badassico.ico')
root.resizable(False,False)
#####Global variables
audiotrack = StringVar()
music_started=False
#music_paused = False
mixer.init()
root.configure(bg = "Black")
createwidgets()

root.mainloop()