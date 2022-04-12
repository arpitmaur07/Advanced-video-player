from tkinter import *
from tkinter.filedialog import askopenfile
from tkVideoPlayer import TkinterVideo

root = Tk()
root.title("Video Player")
root.geometry("800x550")
root.minsize(800,500)
root.configure(bg="#116562")


def open_file():
    file = askopenfile(mode='r', filetypes=[('Video Files', ["*.mp4",'*.avi'])])
    if file is not None:
        b1['state'] = DISABLED
        b1['bg'] = 'white'
        lbl3.pack_forget()
        global filename
        filename = file.name
        global videoplayer
        videoplayer = TkinterVideo(master=root, scaled=True, pre_load=False)
        videoplayer.load(r"{}".format(filename))
        videoplayer.pack(expand=True, fill="both")
        videoplayer.play()



def playAgain():
    videoplayer.play()

def StopVideo():
    b2['state'] = DISABLED
    b2['bg'] = 'white'
    videoplayer.stop()

def PauseVideo():
    videoplayer.pause()
    
def exitWindow():
    root.destroy()    
    root.quit()
    

lbl1 = Label(root, text="Video Player",fg="white",bg='#4a7abc', font="none 25 bold")
lbl1.config(anchor=CENTER)
lbl1.pack(fill='x')

lbl3 = Label(root,text="Click on 'Select Video' button and select video you want to play.",bg='#116562',fg='white',font="none 10 bold")
lbl3.config(anchor=CENTER)
lbl3.pack(pady=30)    



lbl2 = Label(root,bg='#4a7abc')
lbl2.config(anchor=CENTER)
lbl2.pack(side=BOTTOM,fill='x',)


b1 = Button(lbl2, text='Select Video',font="none 10",bg='#4A7A8C',fg='white',activebackground='white',state=NORMAL,activeforeground='#4A7A8C',width=16, command=open_file)
b1.pack(side=LEFT,padx=10, pady=5,anchor="w")

b2 = Button(lbl2, text='PLAY',bg='green',fg='white',font="none 10 ",activebackground='white',activeforeground='green',width=16, command= playAgain)
b2.pack(side=LEFT,padx=10, pady=5,anchor="w")

b3 = Button(lbl2, text='PAUSE',bg='#116562',fg='white',font="none 10",activebackground='white',activeforeground='#116562' ,width=16,command= PauseVideo)
b3.pack(side=LEFT,padx=10, pady=5,anchor="w")

b4 = Button(lbl2, text='STOP',bg='black',fg='white',font="none 10",activebackground='white',activeforeground='black',width=16, command= StopVideo)
b4.pack(side=LEFT,padx=10, pady=5,anchor="w")

b5 = Button(lbl2, text='EXIT',bg='red',fg='white',font="none 10 bold",activebackground='white',activeforeground='red',width=16, command=exitWindow)
b5.pack(side=LEFT,padx=10, pady=5,anchor="w")


root.mainloop()