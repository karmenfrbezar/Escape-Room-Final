import tkinter as tk
import time
import random
import pygame
import os
import sys

# 
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# zvuk
pygame.mixer.init()
pygame.mixer.set_num_channels(32)

try:
    klik = pygame.mixer.Sound(resource_path("tipkanje.wav"))
except:
    klik = None

# prozor
root = tk.Tk()
root.title("Kraj")
root.configure(bg="black")
root.geometry("900x600")

# ================= LOGIN =================

kod = "2834"
attempts = 0

login_frame = tk.Frame(root, bg="black")
login_frame.pack(expand=True, fill="both")

title = tk.Label(
    login_frame,
    text="Konačna šifra",
    bg="black",
    fg="#00ff00",
    font=("Consolas", 20)
)
title.pack(pady=20)

entry = tk.Entry(
    login_frame,
    font=("Consolas", 18),
    bg="black",
    fg="#00ff00",
    insertbackground="#00ff00",
    justify="center",
    #show="*"
)
entry.pack(pady=10)

poruka = tk.Label(
    login_frame,
    text="",
    bg="black",
    fg="red",
    font=("Consolas", 12)
)
poruka.pack(pady=10)

# tekst

text_widget = tk.Text(
    root,
    bg="black",
    fg="#00ff00",
    insertbackground="#00ff00",
    font=("Consolas", 14),
    wrap="word"
)

zavrseno = False

def zatvori(event=None):
    if zavrseno:
        root.destroy()

root.bind("<Return>", zatvori)

text_widget.config(state="disabled")

# efekt tipkanja

def type_text(text):
    text_widget.config(state="normal")

    for char in text:
        text_widget.insert("end", char)
        text_widget.see("end")

        if char.isalnum() and klik:
            pygame.mixer.find_channel(True).play(klik)

        text_widget.update()
        time.sleep(random.uniform(0.02, 0.05))

    text_widget.insert("end", "\n\n")
    text_widget.config(state="disabled")

def print_text(text):
    text_widget.config(state="normal")
    text_widget.insert("end", text + "\n\n")
    text_widget.see("end")
    text_widget.config(state="disabled")
    text_widget.update()

# poruke

messages = [
    "Pozdrav, istraživači!",
    "Ako ste pronašli ovu poruku, uspjeli ste.",
    "Niste pronašli samo ključ laboratorija, pokazali ste znatiželju, logiku, kreativnost i timski rad, osobine koje smo Marta i ja najviše cijenili.",
    "Ovaj laboratorij nikada nije bio zamišljen kao tajna.",
    "Bio je zamišljen kao izazov.",
    "Želio sam ostaviti dokaz da najveća otkrića ne nastaju radom jednog genija, već suradnjom ljudi koji traže rješenja.",
    "Marta je vjerovala da je pravo nasljeđe znanstvenika znanje koje prenese drugima.",
    "Budućnost znanosti sada je u vašim rukama.",
    "I da... Lozinka za izlaz je: G E N I J"
]

atom = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠙⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠁⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣀⣤⣤⣀⣀⡀⠀⢸⠃⠀⠀⠀⠀⠘⡇⠀⢀⣀⣀⣤⣤⣀⡀⠀⠀⠀
⠀⠀⠀⢸⠉⠀⠀⠉⠉⠛⠻⣿⣤⣀⠀⠀⣀⣤⣿⠟⠛⠉⠉⠁⠈⠉⡇⠀⠀⠀
⠀⠀⠀⠘⣧⡀⠀⠀⠀⠀⠀⣇⣀⣽⠿⠿⣯⣀⣸⠀⠀⠀⠀⠀⢀⣼⠃⠀⠀⠀
⠀⠀⠀⠀⠈⠻⣦⡀⠀⣠⣴⡟⠉⠀⢀⡀⠀⠉⢻⣦⣄⠀⢀⣴⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢈⣿⣿⣉⠀⡇⠀⢰⣿⣿⠆⠀⢸⠀⣉⣿⣿⡁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⠟⠁⠀⠙⠻⣧⣀⠀⠉⠉⠀⣀⣼⠟⠋⠀⠈⠻⣦⡀⠀⠀⠀⠀
⠀⠀⠀⢠⡟⠁⠀⠀⠀⠀⠀⡏⠉⣻⣶⣶⣟⠉⢹⠀⠀⠀⠀⠀⠈⢻⡄⠀⠀⠀
⠀⠀⠀⢸⣀⠀⠀⣀⣀⣤⣴⣿⠛⠉⠀⠀⠉⠛⣿⣦⣤⣀⣀⠀⠀⣀⡇⠀⠀⠀
⠀⠀⠀⠈⠉⠛⠛⠉⠉⠁⠀⢸⡄⠀⠀⠀⠀⢠⡇⠀⠈⠉⠉⠛⠛⠉⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⡀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣄⣠⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

# pokretanje

def start_program():
    global zavrseno

    login_frame.destroy()
    text_widget.pack(expand=True, fill="both")

    def step(i=0):
        if i < len(messages):
            type_text(messages[i])
            root.after(600, lambda: step(i + 1))
        else:
            finish()

    def finish():
        global zavrseno

        print_text(atom)
        print_text("================================")
        print_text("Zadatak uspješno izvršen.")
        print_text("Pritisnite ENTER za izlaz...")

        zavrseno = True

    step()

# provjera šifre

def provjeri(event=None):
    global attempts

    if entry.get() == kod:
        start_program()
    else:
        attempts += 1
        poruka.config(text="KRIVA ŠIFRA")
        entry.delete(0, tk.END)

        if attempts >= 3:
            poruka.config(text="Pogledaj privjesak. To bi ti trebalo pomoći u rasporedu. Boje nisu slučajne.")

entry.bind("<Return>", provjeri)

# ==== START =====

root.mainloop()
