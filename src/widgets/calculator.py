# widgets/calculator.py
from tkinter import StringVar, Entry, Button, Frame, Tk

class Calculator:
    def __init__(self, parent_frame: Frame):
        self.var_input = StringVar()
        self._build_ui(parent_frame)

    def _build_ui(self, parent_frame: Frame):
        self.entry = Entry(
            parent_frame, textvariable=self.var_input, font=('arial', 15, 'bold'),
            width=21, bd=10, relief='GROOVE', state='readonly', justify='RIGHT'
        )
        self.entry.grid(row=0, columnspan=4)

        buttons = [
            (7, 1, 0), (8, 1, 1), (9, 1, 2), ('+', 1, 3),
            (4, 2, 0), (5, 2, 1), (6, 2, 2), ('-', 2, 3),
            (1, 3, 0), (2, 3, 1), (3, 3, 2), ('*', 3, 3),
            (0, 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3),
        ]

        for text, row, col in buttons:
            cmd = self._get_button_command(text)
            Button(
                parent_frame, text=str(text), font=('arial', 15, 'bold'),
                command=cmd, bd=5, width=4, pady=10 if text != 0 else 15,
                cursor="hand2"
            ).grid(row=row, column=col)

    def _get_button_command(self, text):
        if text == 'C':
            return self.clear
        if text == '=':
            return self.calculate
        return lambda: self.append(str(text))

    def append(self, value: str):
        current = self.var_input.get() + value
        self.var_input.set(current)

    def clear(self):
        self.var_input.set('')

    def calculate(self):
        try:
            result = eval(self.var_input.get())
            self.var_input.set(str(result))
        except:
            self.var_input.set('Error')
