# todo - backspace and brackets
import tkinter as tk
from pyautogui import press
from PIL import ImageTk, Image


class Calculator:
    def __init__(self):
        # Window creation.
        self.window = tk.Tk()
        self.window.geometry("270x188")
        self.window.resizable(width=False, height=False)

        # Numbers creation.
        c = 1
        r = 5
        for i in range(10):
            button = tk.Button(self.window, text=i, width=2,
                               font=("sans", 14, "bold"))
            button.bind("<Button-1>", self.button_press)
            button.grid(column=c, row=r)
            if i in [0, 3, 6]:
                r -= 1
                c = 1
            else:
                c += 1

        # Signs creation.
        r = 2
        for ch in ["/", "*", "-", "+"]:
            button = tk.Button(self.window, text=ch, width=2,
                               font=("sans", 14, "bold"))
            button.grid(column=4, row=r)
            button.bind("<Button-1>", self.button_press)
            r += 1

        dot_button = tk.Button(self.window, text=".", width=2,
                               font=("sans", 14, "bold"))
        dot_button.bind("<Button-1>", self.button_press)
        dot_button.grid(column=2, row=5)

        clear_button = tk.Button(self.window, text="C", width=2,
                                 font=("sans", 14, "bold"), command=self.clear)
        clear_button.grid(column=3, row=5)

        equal_button = tk.Button(self.window, text="=", width=2,
                                 font=("sans", 14, "bold"), height=2, command=self.show_result)
        equal_button.grid(column=5, row=4, rowspan=2, ipady=7)

        backspace_icon = ImageTk.PhotoImage(Image.open("backspace.png"))
        backspace_button = tk.Button(
            self.window, image=backspace_icon, width=50, height=70, command=lambda: press("backspace"), activebackground="#d9d9d9")
        backspace_button.grid(row=2, column=5, rowspan=2)

        # Entry widget creation (display).
        self.entry_content = tk.StringVar()
        self.entry_content = tk.Entry(self.window, textvariable=self.entry_content,
                                      font=("sans", 14, "bold"))
        self.entry_content.grid(column=1, row=0, columnspan=5, ipady=5)
        self.entry_content.focus_set()
        self.entry_content.bind("<Return>", self.show_result)

        self.window.mainloop()

    # Function that displays the result.
    def show_result(self, *args):
        self.operation_string = self.entry_content.get()
        try:
            result = eval(self.operation_string)
            self.clear()
            self.entry_content.insert(0, result)
        except NameError:
            self.error("The math is incorrect!")
        except SyntaxError:
            pass
        except ZeroDivisionError:
            self.error("You can't divide by zero!")

    # Displays an error message on the display.
    def error(self, message):
        self.clear()
        self.entry_content.insert(0, message)
        self.window.after(1500, self.clear)

    # Clears the display.
    def clear(self):
        last = len(self.entry_content.get())
        self.entry_content.delete(first=0, last=last)

    # Presses a button (sign) pressed on the calculator.
    def button_press(self, event):
        pressed_buttton = event.widget
        press(str(pressed_buttton["text"]))


calculator = Calculator()
