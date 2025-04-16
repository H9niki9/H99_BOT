import customtkinter
import time
import farm
import juwel
import chicken
import Club
import threading
import sys
import json
import os

# Global variables for timer
running = False
countdown_seconds = 10  # Changed from 5 to 10
timer_thread = None
bot_thread = None  # Track the bot thread to be able to stop it

# Du hast vergessen, stop_event zu definieren
stop_event = threading.Event()

# Pfad für die Einstellungsdatei
settings_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings.json")

# Standardeinstellungen
default_settings = {
    "last_option": 0,
    "countdown_time": 10,
    "theme": "System"
}

# Einstellungen laden
def load_settings():
    if os.path.exists(settings_file):
        try:
            with open(settings_file, "r") as f:
                return json.load(f)
        except:
            return default_settings
    return default_settings

# Einstellungen speichern
def save_settings(settings):
    with open(settings_file, "w") as f:
        json.dump(settings, f)

# Lade Einstellungen
settings = load_settings()

def radiobutton_event():
    print(f"RadioButton selected: {radio_var.get()}")
    # Speichere die ausgewählte Option
    settings["last_option"] = radio_var.get()
    save_settings(settings)

def cooldown():
    for i in range(countdown_seconds, 0, -1):
        if stop_event.is_set():
            return
        print(f"Script starts in {i} seconds")
        time.sleep(1)

def update_timer():
    global countdown_seconds, running
    while running and countdown_seconds > 0 and not stop_event.is_set():
        countdown_seconds -= 1
        timer_label.configure(text=f"{countdown_seconds}")
        progress_bar.set(1 - (countdown_seconds / settings["countdown_time"]))
        time.sleep(1)
    
    if running and countdown_seconds == 0 and not stop_event.is_set():
        timer_label.configure(text="Running...")
        progress_bar.set(1)

def start_button_event():
    global running, countdown_seconds, timer_thread, bot_thread
    
    # Reset stop event
    stop_event.clear()
    
    # Reset and start countdown
    countdown_seconds = settings["countdown_time"]
    running = True
    timer_thread = threading.Thread(target=update_timer)
    timer_thread.daemon = True
    timer_thread.start()
    
    # Update status
    status_label.configure(text="Status: Starting...")
    
    print("Start button pressed")
    selected_option = radio_var.get()
    print(f"Starting with option: {selected_option}")
    
    # Run the bot function in a separate thread
    if selected_option == 1:
        bot_thread = threading.Thread(target=run_bot_function, args=(1,))
        bot_thread.daemon = True
        bot_thread.start()
    elif selected_option == 2:
        bot_thread = threading.Thread(target=run_bot_function, args=(2,))
        bot_thread.daemon = True
        bot_thread.start()
    elif selected_option == 3:
        bot_thread = threading.Thread(target=run_bot_function, args=(3,))
        bot_thread.daemon = True
        bot_thread.start()
    elif selected_option == 4:
        bot_thread = threading.Thread(target=run_bot_function, args=(4,))
        bot_thread.daemon = True
        bot_thread.start()
    else:
        print("Please select an option first")
        status_label.configure(text="Status: Please select an option")
        running = False

def run_bot_function(option):
    # This function runs in a separate thread
    if stop_event.is_set():
        return
        
    cooldown()
    
    if stop_event.is_set():
        return
        
    try:
        if option == 1:
            juwel.juwel_function()
        elif option == 2:
            Club.Club_function()
        elif option == 3:
            farm.farm_function()
        elif option == 4:
            chicken.chicken_wing()
    except Exception as e:
        print(f"Error in bot function: {e}")
        status_label.configure(text=f"Error: {str(e)[:30]}...")

def end_button_event():
    global running
    running = False
    status_label.configure(text="Status: Stopped")
    timer_label.configure(text="Stopped")
    progress_bar.set(0)
    print("Script stopped by user")
    
    # Einfach das Programm beenden
    import os
    os._exit(0)  # Beendet das Programm sofort
    stop_event.set()  # Signal all threads to stop
    
    # Forcefully kill the bot thread if it's still running
    if bot_thread and bot_thread.is_alive():
        print("Forcing application to close...")
        # Give a short delay for UI to update
        app.after(500, lambda: sys.exit(0))

# Theme-Wechsler-Funktion
def change_appearance_mode(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)
    settings["theme"] = new_appearance_mode
    save_settings(settings)

# Countdown-Zeit ändern
def change_countdown_time(value):
    global countdown_seconds
    settings["countdown_time"] = int(value)
    countdown_seconds = settings["countdown_time"]
    timer_label.configure(text=str(countdown_seconds))
    save_settings(settings)
    countdown_label.configure(text=f"Countdown: {int(value)}s")

app = customtkinter.CTk()
app.title("H99_BOT")
app.geometry("500x450")  # Erhöhte Höhe für zusätzliche Elemente
app.grid_columnconfigure((0, 1), weight=1)

# Setze das Theme aus den Einstellungen
customtkinter.set_appearance_mode(settings["theme"])

# Variable for RadioButtons
radio_var = customtkinter.IntVar(value=settings["last_option"])

# Title label und Theme-Switcher in einem Frame
title_frame = customtkinter.CTkFrame(app, fg_color="transparent")
title_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="ew")
title_frame.grid_columnconfigure(0, weight=1)

title_label = customtkinter.CTkLabel(title_frame, text="H99_BOT Controller", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, sticky="w")

# Theme switcher
appearance_mode_menu = customtkinter.CTkOptionMenu(
    title_frame, 
    values=["System", "Light", "Dark"],
    command=change_appearance_mode
)
appearance_mode_menu.grid(row=0, column=1, padx=10, sticky="e")
appearance_mode_menu.set(settings["theme"])

# Timer display mit Fortschrittsbalken
timer_frame = customtkinter.CTkFrame(app, fg_color="transparent")
timer_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=(5, 10), sticky="ew")

timer_label = customtkinter.CTkLabel(timer_frame, text=str(settings["countdown_time"]), font=("Arial", 36, "bold"))
timer_label.pack(pady=(0, 5))

progress_bar = customtkinter.CTkProgressBar(timer_frame, width=400)
progress_bar.pack(pady=(0, 5))
progress_bar.set(0)

# Countdown-Zeit-Einstellung
countdown_frame = customtkinter.CTkFrame(app, fg_color="transparent")
countdown_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=(0, 10), sticky="ew")

countdown_label = customtkinter.CTkLabel(countdown_frame, text=f"Countdown: {settings['countdown_time']}s")
countdown_label.pack(side="top", pady=(0, 5))

countdown_slider = customtkinter.CTkSlider(
    countdown_frame, 
    from_=5, 
    to=30, 
    number_of_steps=25,
    command=change_countdown_time
)
countdown_slider.pack(side="bottom", fill="x", padx=10)
countdown_slider.set(settings["countdown_time"])

# RadioButtons
radiobutton_2 = customtkinter.CTkRadioButton(app, text="Emergency Hamburg Club (23k p/h) - Recommended", 
                                           variable=radio_var, value=2,
                                           command=radiobutton_event)
radiobutton_2.grid(row=3, column=0, padx=20, pady=(5, 5), sticky="w")

radiobutton_1 = customtkinter.CTkRadioButton(app, text="Emergency Hamburg Jewelry (13k p/h)", 
                                           variable=radio_var, value=1,
                                           command=radiobutton_event)
radiobutton_1.grid(row=4, column=0, padx=20, pady=(5, 5), sticky="w")

radiobutton_3 = customtkinter.CTkRadioButton(app, text="Emergency Hamburg Farm", 
                                           variable=radio_var, value=3,
                                           command=radiobutton_event)
radiobutton_3.grid(row=5, column=0, padx=20, pady=(5, 5), sticky="w")

radiobutton_4 = customtkinter.CTkRadioButton(app, text="AFK Chicken Wing", 
                                           variable=radio_var, value=4,
                                           command=radiobutton_event)
radiobutton_4.grid(row=6, column=0, padx=20, pady=(5, 5), sticky="w")

# Button frame for Start and End buttons
button_frame = customtkinter.CTkFrame(app, fg_color="transparent")
button_frame.grid(row=3, column=1, rowspan=4, padx=20, pady=20, sticky="nsew")
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_rowconfigure((0, 1), weight=1)

# Start Button
start_button = customtkinter.CTkButton(button_frame, text="Start", command=start_button_event)
start_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# End Button
end_button = customtkinter.CTkButton(button_frame, text="End", command=end_button_event, fg_color="#D32F2F")
end_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Status label
status_label = customtkinter.CTkLabel(app, text="Status: Ready", font=("Arial", 12))
status_label.grid(row=7, column=0, columnspan=2, padx=20, pady=(10, 10), sticky="ew")

# Add credits section
credits_frame = customtkinter.CTkFrame(app)
credits_frame.grid(row=8, column=0, columnspan=2, padx=20, pady=(5, 10), sticky="ew")

credits_text = """
Developed with Python + PyAutoGUI
UI created with CustomTkinter
UI design assisted by AI
Programmed by H9niki9

This software is not affiliated with Roblox or Emergency Hamburg.
© 2023 All Rights Reserved
"""

credits_label = customtkinter.CTkLabel(
    credits_frame, 
    text=credits_text, 
    font=("Arial", 10),
    justify="center"
)
credits_label.pack(padx=10, pady=10)

app.mainloop()