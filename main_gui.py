import customtkinter as ctk
from threading import Thread
from password_cracker import brute_force, dictionary_attack, CrackerState

state = CrackerState()

def run_crack():
    password = password_entry.get()
    mode = mode_option.get()
    result_label.configure(text="")
    crack_button.configure(state="disabled")
    stop_button.configure(state="normal")
    state.stop = False

    if not password:
        result_label.configure(text="Please enter a password.")
        crack_button.configure(state="normal")
        stop_button.configure(state="disabled")
        return

    if mode == "Brute Force":
        generator = brute_force(password, state)
    else:
        try:
            with open("common_passwords.txt", "r") as file:
                words = file.readlines()
        except FileNotFoundError:
            result_label.configure(text="Wordlist not found.")
            crack_button.configure(state="normal")
            stop_button.configure(state="disabled")
            return
        generator = dictionary_attack(password, words, state)

    for guess, attempts, elapsed in generator:
        current_guess_label.configure(text=f"Guess: {guess}")
        attempts_label.configure(text=f"Attempts: {attempts}")
        time_label.configure(text=f"Time: {elapsed} sec")
        app.update()
        if guess == password:
            result_label.configure(
                text=f"Password Cracked!"
            )
            break

    if state.stop:
        result_label.configure(text="Cracking stopped by user.")
    
    crack_button.configure(state="normal")
    stop_button.configure(state="disabled")

def start_cracking():
    Thread(target=run_crack).start()

def stop_cracking():
    state.stop = True

# GUI setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("500x490")
app.title("Advanced Password Cracker")

title = ctk.CTkLabel(app, text="Password Cracker\nBrute Force & Dictionary Attack", font=("Arial",18, "bold"))
title.pack(pady=15)

password_entry = ctk.CTkEntry(app, width=300, show="*", placeholder_text="Enter Password")
password_entry.pack(pady=10)


def toggle_password():
    if show_password_checkbox.get() == 1:
        password_entry.configure(show="")
    else:
        password_entry.configure(show="*")

show_password_checkbox = ctk.CTkCheckBox(app, text="Show Password", command=toggle_password)
show_password_checkbox.pack(pady=5)

mode_option = ctk.CTkOptionMenu(app, values=["Brute Force", "Dictionary Attack"])
mode_option.set("Brute Force")
mode_option.pack(pady=10)

crack_button = ctk.CTkButton(app, text="Start Cracking", command=start_cracking)
crack_button.pack(pady=10)

stop_button = ctk.CTkButton(app, text="Stop", command=stop_cracking, fg_color="red")
stop_button.pack(pady=5)
stop_button.configure(state="disabled")

current_guess_label = ctk.CTkLabel(app, text="Guess: ", font=("Arial", 14))
current_guess_label.pack(pady=5)

attempts_label = ctk.CTkLabel(app, text="Attempts: 0", font=("Arial", 14))
attempts_label.pack(pady=5)

time_label = ctk.CTkLabel(app, text="Time: 0 sec", font=("Arial", 14))
time_label.pack(pady=5)

result_label = ctk.CTkLabel(app, text="", wraplength=460, font=("Arial", 14))
result_label.pack(pady=20)

app.mainloop()
