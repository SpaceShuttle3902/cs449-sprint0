# gui.py using tkinter
# This assignment includes: text, lines, a check box, and radio buttons

#We first import the modules we need
import tkinter as tk            
from tkinter import ttk         

#Our main window
def main():
    root = tk.Tk()
    #The window title
    root.title("Sprint0 GUI Demo")       
    # The window size
    root.geometry("600x400")             

    # 1) TEXT 

    # Create a big title label
    title_label = ttk.Label(root, text="Sprint 0 GUI Demo", font=("Segoe UI", 16))
    #adding vertical spacing while placing widgets
    title_label.pack(pady=10)

    # Create a smaller label (more text)
    info_label = ttk.Label(root, text="Project includes: text, line, checkbox, radio buttons")
    info_label.pack()

    # 2) Canvas line 
    canvas = tk.Canvas(root, height=20)
    canvas.pack(fill="x", padx=10)  # fill = "x" stretches horizontally

    # Here we draw a horizontal line
    canvas.create_line(10, 10, 500, 10, width=2)

    canvas.create_line(10, 15, 500, 15, width=2)


    #Checkbox
    #Here we store true and false 
    record_var = tk.BooleanVar(value=False)

    # Checkbutton is a checkbox widget. It will update record_var automatically.
    record_checkbox = ttk.Checkbutton(root, text="Record game", variable=record_var)
    record_checkbox.pack(anchor="w", padx=20, pady=8)  # anchor="w" left-aligns it

   
    # 3.) Radio Buttons

    #There are only 3 selections: English, Hexagon, Diamond

    # The StringVar stores which radio option is selected
    board_var = tk.StringVar(value="English")

    # Here we put the radio buttons inside a frame (box with a title)
    board_frame = ttk.LabelFrame(root, text="Board Type")
    board_frame.pack(fill="x", padx=20, pady=10)

    # Each Radiobutton sets board_var to its value when clicked
    ttk.Radiobutton(board_frame, text="English", variable=board_var, value="English").pack(anchor="w", padx=10)
    ttk.Radiobutton(board_frame, text="Hexagon", variable=board_var, value="Hexagon").pack(anchor="w", padx=10)
    ttk.Radiobutton(board_frame, text="Diamond", variable=board_var, value="Diamond").pack(anchor="w", padx=10)

    # Here we add a status label to display current selections, added for visuals and confirming that buttons/widgets work.
    status_label = ttk.Label(root, text="")
    status_label.pack(pady=5)

    # This button will show checkbox and radio button values
    def show_settings():
        status_label.config(
            text=f"Record game: {record_var.get()} | Board: {board_var.get()}"
        )

    show_button = ttk.Button(root, text="Show Current Settings", command=show_settings)
    show_button.pack(pady=5)



    #This starts the loop and keeps it open
    root.mainloop()


# This makes sure main() runs only when you run this file directly.
if __name__ == "__main__":
    main()
