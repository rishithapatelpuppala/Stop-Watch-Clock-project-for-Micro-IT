import tkinter as tk
from datetime import datetime
import time
import threading
root = tk.Tk()
root.title("Clock + Stopwatch")
root.geometry("400x300")
root.minsize(300, 250)
root.configure(bg="#f0f0f0")
clock_label = tk.Label(root, font=("Arial", 20), bg="#f0f0f0", fg="black")
clock_label.pack(pady=10)
def update_clock():
    now = datetime.now().strftime("%H:%M:%S")
    clock_label.config(text="Current Time: " + now)
    root.after(1000, update_clock)
update_clock()
stopwatch_label = tk.Label(root, text="00:00:00", font=("Arial", 40), bg="#f0f0f0", fg="blue")
stopwatch_label.pack(pady=20)
start_time = 0
running = False
def format_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02}:{m:02}:{s:02}"
def run_stopwatch():
    global start_time
    while running:
        elapsed = time.time() - start_time
        formatted = format_time(elapsed)
        stopwatch_label.config(text=formatted)
        time.sleep(0.1)
def start():
    global running, start_time
    if not running:
        running = True
        start_time = time.time() - elapsed_time
        threading.Thread(target=run_stopwatch, daemon=True).start()
def stop():
    global running, elapsed_time
    if running:
        running = False
        elapsed_time = time.time() - start_time
def reset():
    global elapsed_time, running
    running = False
    elapsed_time = 0
    stopwatch_label.config(text="00:00:00")
elapsed_time = 0
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)
start_btn = tk.Button(button_frame, text="Start", font=("Arial", 14), command=start, width=8)
start_btn.grid(row=0, column=0, padx=5)
stop_btn = tk.Button(button_frame, text="Stop", font=("Arial", 14), command=stop, width=8)
stop_btn.grid(row=0, column=1, padx=5)
reset_btn = tk.Button(button_frame, text="Reset", font=("Arial", 14), command=reset, width=8)
reset_btn.grid(row=0, column=2, padx=5)
root.mainloop()