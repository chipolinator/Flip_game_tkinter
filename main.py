import tkinter as tk
import random


class Flip(tk.Tk):

    # Возможные ходы
    DIRECTIONS = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
    # Позиции всех кнопок
    POSITION_MAPPING = {(0, 0): 0, (1, 0): 1, (2, 0): 2,
                        (0, 1): 3, (1, 1): 4, (2, 1): 5,
                        (0, 2): 6, (1, 2): 7, (2, 2): 8}

    def __init__(self):
        super().__init__()
        self.geometry("530x550")
        self.buttons, self.frames = [], []
        self.put_main_frames()

    def put_main_frames(self):
        self.text_lbl = tk.Label(self,
                                 text="Правила игры: \n На поле 3x3 случайным образом \n "
                                      "расположены белые и черные квадраты. \n При нажатии на квадрат \n "
                                      "он и его соседи по горизонтали и вертикаали \n меняют цвета на противоположный"
                                      "\n Цель: получить поле из белых квадратов\n Кликните для начала игры.",
                                 font=("Times New Roman", 15))
        self.text_lbl.pack(pady=150)
        self.bind("<Button-1>", self.add_buttons)

    def add_buttons(self, event):
        self.unbind("<Button-1>")
        self.text_lbl.pack_forget()

        for i in range(3):
            # Три фрейма - три строчки
            frame = tk.Frame()
            frame.pack()
            self.frames.append(frame)
            for j in range(3):
                # Добавление кнопок на фреймы со случайным значением бэкграунда
                button = tk.Button(frame,
                                   command=lambda i=i, j=j: self.change_color(i, j),
                                   bg=random.choice(['black', 'white']),
                                   height=10, width=20)
                button.pack(side=tk.LEFT, padx=10, pady=10)
                self.buttons.append(button)

    def change_color(self, i, j):
        # Применяем все действия если они возможны
        for direction in self.DIRECTIONS:
            new_x, new_y = j + direction[0], i + direction[1]

            # т.е если они лежат в этом промежутке меняем значения бэкграунда на противоположное
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                button_index = self.POSITION_MAPPING[(new_x, new_y)]
                current_color = self.buttons[button_index].cget('bg')

                new_color = 'black' if current_color == 'white' else 'white'
                self.buttons[button_index].config(bg=new_color)

        # Проверяем победили ли мы
        self.check_for_victory()

    def check_for_victory(self):
        # Если победили удаляем все кнопки и все фреймы (для этого мы заранее составили их список)
        if all(button.cget('bg') == 'white' for button in self.buttons):
            for button in self.buttons:
                button.destroy()
            self.buttons.clear()

            for frame in self.frames:
                frame.destroy()
            self.frames.clear()

            self.put_main_frames()
            self.text_lbl.config(text="Вы победили!\n Кликните для начала новой игры.")


if __name__ == '__main__':
    app = Flip()
    app.mainloop()
