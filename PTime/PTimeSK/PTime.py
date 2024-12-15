import customtkinter as ctk
import CTkMessagebox as msgbox
import time
import threading
import winsound

# Okno
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("_internal/style.json")
window = ctk.CTk()
window.title("PTime")
window.resizable(False, False)
window.geometry("300x200")
window.iconbitmap("_internal/icon.ico")

# Funkcie
def start():
    timer = threading.Thread(target=time_count)
    timer.daemon = True
    timer.start()
    timer.join()

def display_time(remain, max_time):
    hours, remain_sec = divmod(remain, 3600)
    minutes, sec = divmod(remain_sec, 60)

    remain_time.configure(text=f"{hours}:{minutes}:{sec}")

    time_progress_bar.set((remain)/(int(max_time)))

def time_count():
    try:
        max_time = int(time_value.get())*60
        remain = int(time_value.get())*60

        while remain != 0:
            display_time(remain, max_time)
            time.sleep(1)
            remain -= 1

        remain_time.configure(text="")
        msgbox.CTkMessagebox(message="Čas na prestávku!", icon="info", title="PTime", sound=False)
        winsound.PlaySound("notification.wav", winsound.SND_FILENAME)
    except ValueError:
        time_value.delete(0, ctk.END)
        msgbox.CTkMessagebox(message="Chyba: Zadajte celé číslo.", title="PTime", sound=False)
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

# Prvky
minute_label = ctk.CTkLabel(window, text="Zadajte interval v minutách:")
minute_label.pack()

time_value = ctk.CTkEntry(window, placeholder_text="30")
time_value.pack()

start_button = ctk.CTkButton(window, text="Start", command=start)
start_button.pack(padx=10, pady=10)

remain_time = ctk.CTkLabel(window, text="", anchor="center")
remain_time.pack()

time_progress_bar = ctk.CTkProgressBar(window)
time_progress_bar.set(0)
time_progress_bar.pack()

window.mainloop()