import pygame
import tkinter as tk
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk
import os

music_player = tk.Tk()
music_player.title("Music Player")
music_player.geometry("450x350")
music_player.config(bg="#fff")
#The askdirectory presents the user with a popup for directory selection.
directory = askdirectory()
#chdir() changes the current working directory to the given path. It returns None in all the cases.
os.chdir(directory)
#listdir() returns a list containing the names of the entries in the directory given by path. But it does not include the special entries '.' and '..' even if they are present in the directory.
song_list = os.listdir()

#to provide a scrollbar for the listbox
scrollbar = tk.Scrollbar(music_player)
#list all the files in the directory chosen
play_list = tk.Listbox(music_player, font="Helvetica 12 bold", bg="#404042", selectmode=tk.SINGLE)
#populate the list
for item in song_list:
        #if condition to only add songs to the list, excluding all other non-music files
        if(item[-4:] == '.mp3'):
                pos = 0
                play_list.insert(pos, item)
                pos += 1
pygame.init()
pygame.mixer.init()

#variable for the toggle button function
check = True

#function to use a single button as a toggle button
def play_pause():
        global check
        if(check):
                pygame.mixer.music.pause()
                icon3.configure(file="play-button-arrowhead.png")
                check = False
        else:
                pygame.mixer.music.unpause()
                icon3.configure(file="pause.png")
                check = True

def play():
	pygame.mixer.music.load(play_list.get(tk.ACTIVE))
	var.set(play_list.get(tk.ACTIVE)[:-4])
	pygame.mixer.music.play()
def stop():
	pygame.mixer.music.stop()

icon1 = tk.PhotoImage(file="music.png")
icon2 = tk.PhotoImage(file="stop.png")
icon3 = tk.PhotoImage(file="pause.png")

Button1 = tk.Button(music_player, image=icon1, command=play)
Button2 = tk.Button(music_player, image=icon2, command=stop)
Button3 = tk.Button(music_player, image=icon3, command=play_pause)

var = tk.StringVar()
song_title = tk.Label(music_player, font="Helvetica 20 bold", textvariable=var, bg="#fff")
scrollbar.pack(side="right", fill="y")
play_list.pack(fill="both", expand="no")
play_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=play_list.yview)
song_title.place(x=240, y=230, anchor="center")
Button1.place(x=100, y=300)
Button3.place(x=170, y=300)
Button2.place(x=240, y=300)
music_player.mainloop()
