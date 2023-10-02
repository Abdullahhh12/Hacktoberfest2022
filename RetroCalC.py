import tkinter as tk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Retro Calculator")
        self.window.geometry("300x300")

        # Create the display
        self.display = tk.Entry(self.window, width=30)
        self.display.grid(row=0, column=0, columnspan=3)

        # Create the buttons
        self.buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]

        for row in range(4):
            for column in range(4):
                button = tk.Button(self.window, text=self.buttons[row][column], command=self.on_button_click)
                button.grid(row=row + 1, column=column)

        # Bind the window to the keyboard
        self.window.bind("<Key>", self.on_key_press)

        # Start the mainloop
        self.window.mainloop()

    def on_button_click(self, event):
        button_text = event.widget["text"]

        if button_text == "=":
            self.evaluate()
        elif button_text == "C":
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, button_text)
        print(self.display.get())

    def on_key_press(self, event):
        key = event.char

        if key in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "+", "-", "*", "/"]:
            self.on_button_click(tk.Button(text=key))

    def evaluate(self):
        expression = self.display.get()
        result = eval(expression)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, result)

if __name__ == "__main__":
    calculator = Calculator()
