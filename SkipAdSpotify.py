import customtkinter as ctk
import pyautogui
import time
import os
import keyboard
from PIL import Image, ImageTk
import webbrowser
import tkinter as tk

def close_spotify():
    os.system('taskkill /f /im Spotify.exe')
    os.system('start Spotify.exe')
    time.sleep(4)
    pyautogui.press('space')

def open_github(event=None):
    webbrowser.open("https://github.com/NiclawYTB")
app = ctk.CTk()
app.iconbitmap("spot.ico")
app.geometry("300x300")
app.title("SkipAdSpotify ShortCut")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
label = ctk.CTkLabel(app, text="Bienvenue faites SHIFT + G pour skip la pub Spotify", text_color="white")
label.pack(pady=20)
# NICLAWONTHETOP
github_image = Image.open("githubImg.png")
github_image = github_image.resize((55, 35))
github_photo = ImageTk.PhotoImage(github_image)
github_label = tk.Label(app, image=github_photo, cursor="hand2")
github_label.pack(pady=10, padx=50)
github_label.bind("<Button-1>", open_github)
keyboard.add_hotkey('shift+g', close_spotify)

# Démarrer l'application
app.mainloop()
