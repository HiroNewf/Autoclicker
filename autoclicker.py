import tkinter as tk
import threading
import time
import pyautogui
import keyboard

# The autoclicker itself
class Autoclicker:
    def __init__(self, button, click_interval, repeat_forever=True, num_repeats=None):
        self.button = button
        self.click_interval = click_interval
        self.repeat_forever = repeat_forever
        self.num_repeats = num_repeats
        self.is_running = False
        self.click_count = 0

    def autoclick_thread(self, gui_instance):
        while self.is_running:
            time.sleep(self.click_interval)
            if self.button in ['left', 'right', 'middle']:
                pyautogui.click(button=self.button)
            else:
                keyboard.press(self.button)
                keyboard.release(self.button)
            self.click_count += 1

            if not self.repeat_forever and self.num_repeats is not None and self.click_count >= self.num_repeats:
                self.stop_autoclicker(gui_instance)

    def start_autoclicker(self, gui_instance):
        self.is_running = True
        autoclick_thread = threading.Thread(target=self.autoclick_thread, args=(gui_instance,))
        autoclick_thread.start()
        print(f"Autoclicker started for button '{self.button}'. Press 'Ctrl + C' to stop.")

    def stop_autoclicker(self, gui_instance):
        self.is_running = False
        print("Autoclicker stopped. Total clicks:", self.click_count)
        gui_instance.on_autoclicker_stopped()

# Man I really hate making GUI's, but here we are 
class AutoclickerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hiro's Incredible Autoclicker")
        self.root.geometry("290x185")
        self.root.resizable(False, False)
        self.root.configure(bg="#3D2E4D")

        button_label = tk.Label(root, text="Button:", bg="#3D2E4D", fg="#B3A5C0")
        button_label.grid(row=0, column=0, pady=5, padx=10, sticky="e")

        self.button_entry = tk.Entry(root, width=5)
        self.button_entry.grid(row=0, column=1, pady=5, padx=5, sticky="w")

        self.num_repeats_button = tk.Button(root, text="Repeat ___ Times", command=self.get_num_repeats, bg="#30243D", fg="#C7CCDB", activebackground="#706993", relief=tk.RAISED)
        self.num_repeats_button.grid(row=3, column=0, pady=3, padx=5, sticky="w")

        self.repeat_forever_button = tk.Button(root, text="Repeat Forever", command=lambda: self.toggle_repeat("forever"), bg="#30243D", fg="#C7CCDB", activebackground="#706993", relief=tk.RAISED)
        self.repeat_forever_button.grid(row=3, column=1, pady=3, padx=5, sticky="e")

        self.interval_label = tk.Label(root, text="Press Interval:", bg="#3D2E4D", fg="#B3A5C0")
        self.interval_label.grid(row=2, column=0, pady=5, padx=10, sticky="e")

        self.interval_entry = tk.Entry(root, width=5)
        self.interval_entry.grid(row=2, column=1, pady=5, padx=5, sticky="w")

        start_button = tk.Button(root, text="Start", command=self.start_autoclicker, bg="#30243D", fg="#C7CCDB", activebackground="#706993")
        start_button.grid(row=4, column=0, pady=10)

        stop_button = tk.Button(root, text="Stop", command=self.stop_autoclicker, bg="#30243D", fg="#C7CCDB", activebackground="#706993")
        stop_button.grid(row=4, column=1, pady=10)

        self.autoclicker = None
        self.selected_button = None

        self.root.update()
        self.center_window(None)

        self.num_repeats_button.bind("<Button-1>", lambda event: self.toggle_repeat("num_repeats"))
        self.repeat_forever_button.bind("<Button-1>", lambda event: self.toggle_repeat("forever"))
        self.num_repeats_button.bind("<Enter>", lambda event: self.change_button_color(self.num_repeats_button))
        self.num_repeats_button.bind("<Leave>", lambda event: self.restore_button_color(self.num_repeats_button))
        self.repeat_forever_button.bind("<Enter>", lambda event: self.change_button_color(self.repeat_forever_button))
        self.repeat_forever_button.bind("<Leave>", lambda event: self.restore_button_color(self.repeat_forever_button))
	# This totaly centers the GUI on the window (shhhh)
    def center_window(self, event):
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 2) - (h // 2)
        self.root.geometry('+%d+%d' % (x, y))

    def toggle_repeat(self, mode):
        if mode == "forever":
            self.num_repeats_button.config(bg="#30243D", relief=tk.RAISED)
            self.repeat_forever_button.config(bg="#706993", relief=tk.SUNKEN)
            self.selected_button = self.repeat_forever_button
        elif mode == "num_repeats":
            self.repeat_forever_button.config(bg="#30243D", relief=tk.RAISED)
            self.num_repeats_button.config(bg="#706993", relief=tk.SUNKEN)
            self.selected_button = self.num_repeats_button

    def get_num_repeats(self, event=None):
        repeat_window = tk.Toplevel(self.root)
        repeat_window.title("Enter Number of Presses")
        repeat_window.geometry("200x100")
        repeat_window.configure(bg="#3D2E4D")

        repeat_label = tk.Label(repeat_window, text="Enter Number of Presses:", bg="#3D2E4D", fg="#B3A5C0")
        repeat_label.pack(pady=10)

        repeat_entry = tk.Entry(repeat_window)
        repeat_entry.pack(pady=5)

        confirm_button = tk.Button(repeat_window, text="Confirm", command=lambda: self.confirm_num_repeats(repeat_window, repeat_entry),
                                   bg="#30243D", fg="#C7CCDB", activebackground="#706993", relief=tk.RAISED)
        confirm_button.pack(pady=5)

    def confirm_num_repeats(self, window, entry):
        num_repeats = entry.get()
        if num_repeats.isdigit():
            self.num_repeats_button["text"] = f"Repeat {num_repeats} Times"
            window.destroy()
        else:
            error_label = tk.Label(window, text="Please enter a valid number", fg="red", bg="#3D2E4D")
            error_label.pack(pady=5)

    def start_autoclicker(self):
        button_to_click = self.button_entry.get().lower()
        click_interval = float(self.interval_entry.get()) if self.interval_entry.get() else 0.5
        repeat_forever = self.selected_button == self.repeat_forever_button
        num_repeats = int(self.num_repeats_button["text"].split()[-2]) if not repeat_forever else None

        if not button_to_click:
            self.show_error("Please enter a button to click.")
            return

        if self.autoclicker:
            self.stop_autoclicker()

        self.button_entry.config(state=tk.DISABLED)
        self.interval_entry.config(state=tk.DISABLED)
        self.num_repeats_button.config(state=tk.DISABLED)
        self.repeat_forever_button.config(state=tk.DISABLED)

        self.restore_button_color(self.num_repeats_button)
        self.restore_button_color(self.repeat_forever_button)

        self.autoclicker = Autoclicker(button_to_click, click_interval, repeat_forever, num_repeats)
        self.autoclicker.start_autoclicker(self)

    def stop_autoclicker(self):
        if self.autoclicker:
            self.autoclicker.stop_autoclicker(self)

    def on_autoclicker_stopped(self):
        self.button_entry.config(state=tk.NORMAL)
        self.interval_entry.config(state=tk.NORMAL)
        self.num_repeats_button.config(state=tk.NORMAL)
        self.repeat_forever_button.config(state=tk.NORMAL)

        self.restore_button_color(self.num_repeats_button)
        self.restore_button_color(self.repeat_forever_button)

    def show_error(self, message):
        error_label = tk.Label(self.root, text=message, fg="red", bg="#3D2E4D")
        error_label.grid(row=5, column=0, columnspan=2, pady=5, padx=10)

    def change_button_color(self, button):
        button.config(bg="#706993", relief=tk.SUNKEN)

    def restore_button_color(self, button):
        if self.selected_button != button:
            button.config(bg="#30243D", relief=tk.RAISED)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoclickerGUI(root)
    root.mainloop()
