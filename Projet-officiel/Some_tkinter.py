
import tkinter as tk
from collections.abc import Callable

from tkinter import messagebox


def reinit(exe: Callable):
    print("reinitialize")
    ttl = "WARNING: USE YOUR BRAIN AND READ THIS"
    msg = """You're either about to do something stupid or willingfully reinitialize your masterpiece. Are you sure you want to proceed?"""
    response = messagebox.askyesno(ttl, msg, icon="warning")
    if response:
        exe()
        print("reinit successful")
    else:
        print("reinit aborted")

TEXT_DESC = "Congrats on your brand new project! You can copy the data of your map with the following button:"
default_copy = "Lorem ipsum latino brainrot shit amen j'ai un visage detruit crisse de tabernac"

#feat. Gemini AI
def copy_win(copy_text: str = default_copy):
    #if too long
    show_text = copy_text
    if len(show_text) > 50:
        show_text = show_text[:49] + "[...]"

    root = tk.Tk()
    root.title("Main Application")
    root.geometry("700x500")
    root.withdraw()

    popup = tk.Toplevel(root)
    popup.title("Saving Project")

    # Make the popup appear centered relative to the main window
    popup.geometry("500x500")

    def on_popup_close():
        # Destroying root will close the popup and exit the entire application
        root.destroy()
    popup.protocol("WM_DELETE_WINDOW", on_popup_close)

    # Optional: Prevent interacting with the main window until popup is closed
    #popup.grab_set()

    #labels with copy text and description
    label = tk.Label(popup, text=TEXT_DESC, font=("Arial", 10), wraplength=300)
    label.pack(pady=(30, 5))

    border_frame = tk.Frame(popup, bg="black")
    border_frame.pack(pady=50)

    entry = tk.Label(border_frame, text=show_text, font=("Arial", 11), width=40,)
    entry.pack(padx=2, pady=2)

    writing = tk.Entry(popup, font=("Arial", 11))
    writing.pack(padx=30)

    def copy_action():
        text_to_copy = label["text"]

        # Clear the system clipboard and append the new text
        root.clipboard_clear()
        root.clipboard_append(copy_text)

        # UI feedback: Change button appearance to show it worked
        copy_button.config(text="Copied!", bg="#4CAF50", fg="white", state="disabled")

        # # Automatically close the popup after 1 second (1000 milliseconds)
        def close():
            #popup.destroy()
            root.destroy()
        #popup.after(1000, close)

    # 4. Add the Copy Button
    copy_button = tk.Button(
        popup,
        text="Copy to Clipboard",
        command=copy_action,
        bg="#0078D4",
        fg="white",
        padx=10,
        pady=5
    )
    copy_button.pack(pady=10)

    tk.mainloop()

copy_win()
