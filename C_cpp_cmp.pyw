import tkinter as tk
from tkinter import filedialog
import os



def compile(cmd, ext):
    file = filedialog.askopenfilename(title="Select a file")
    if file.endswith(f".{ext}"):
        os.system(f'"{cmd} "{file}" -o "{file[:-4]}.exe"')
    else:
        print("[+] Please select a cpp file")

    os.system(f'"{file[:-4]}.exe" & PAUSE')

# Create the main application window
app = tk.Tk()
app.title("Option Selection")

# Set the window size
app.geometry("400x150")  # Width x Height
app.configure(bg="azure3")
# Variable to store the user's selection
selected_option = None
selected_ext = None

# Define a function to set the selected option to 'Option 1'
def select_option1():
    global selected_option, selected_ext
    selected_option = 'g++'
    selected_ext = "cpp"
    app.destroy()  # Close the window

# Define a function to set the selected option to 'Option 2'
def select_option2():
    global selected_option, selected_ext
    selected_option = 'gcc'
    selected_ext = "c"
    app.destroy()  # Close the window

# Create two buttons for option selection, displayed horizontally
button1 = tk.Button(app, text="C++", command=select_option1, width=15, height=5, bg="#E3CF57", fg='black')
button2 = tk.Button(app, text="C", command=select_option2, width=15, height=5, bg="#E3CF57", fg="black")

# Place the buttons in the window horizontally
button1.pack(side=tk.LEFT, padx=20)
button2.pack(side=tk.RIGHT, padx=20)

# Start the Tkinter main loop
app.mainloop()

# Print the selected option after the window is closed
if selected_option is not None and selected_ext is not None:
    compile(selected_option, selected_ext)
else:
    print("No option selected")
