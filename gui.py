import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw


# Получаем координаты курсора мыши и реализуем рисование
def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill="black", width=8)
    draw.line([x1, y1, x2, y2], fill='black', width=8)


# Сохранение нарисованного в png
def save_image():
    FILENAME = 'image.png'
    out = img.resize(RESIZE)  # Преобразуем изображение в 28x28 пикселей
    out.save(FILENAME)


# Очистка холста
def clear():
    canvas.delete(tk.ALL)


# Создаем окно
root = tk.Tk()

# Размер окна приложения
WIDTH = 900
HEIGHT = 600

root.geometry(f"{WIDTH}x{HEIGHT}+0+0")  # установка размера окна приложения с координатами (0,0) в левом верхнем углу
root.resizable(False, False)
root.title("Number recognizer")
frame_left = tk.Frame(root, bg="#1d5d80", width=WIDTH // 2 - 10, height=HEIGHT - 100)
frame_right = tk.Frame(root, bg="#1d5d80", width=WIDTH // 2 - 10, height=HEIGHT - 100)
frame_top = tk.Frame(root, bg="#358abf", width=WIDTH, height=70)

frame_left.pack(side='left', padx=0)
frame_right.pack(side='right', padx=0)
frame_top.place(x=0, y=0)

# Установка заднего фона
root.config(bg="#114a69")  # Установка цвета заднего фона

CANVAS_WIDTH = 300  # Ширина полотна
CANVAS_HEIGHT = 300
WHITE = (255, 255, 255)
RESIZE = (28, 28)

# Создаем рамку
canvas_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
canvas_frame.place(x=CANVAS_WIDTH // 2 - 80, y=CANVAS_HEIGHT // 2, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)

# Создаем холст внутри рамки
canvas = tk.Canvas(canvas_frame, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)  # Отображаем холст

# Привязываем обработчики событий мыши к холсту
canvas.bind("<B1-Motion>", paint)

# Копия холста на которую сохраняется нарисованная цифра
img = Image.new('RGB', (CANVAS_WIDTH, CANVAS_HEIGHT), WHITE)
draw = ImageDraw.Draw(img)

# Создаем, отображаем и настраиваем положение кнопок
clear_button = tk.Button(root, text="Очистить", command=clear, bg="#358abf",
                         fg="black", font=("Helvetica", 16), relief='flat')
guess_button = tk.Button(root, text="Распознать", command=save_image, bg="#358abf",
                         fg="black", font=("Helvetica", 16), relief='flat')

clear_button.place(x=CANVAS_WIDTH // 2 + 15, y=HEIGHT - 120)
guess_button.place(x=CANVAS_WIDTH * 2 + 10, y=HEIGHT - 120)

text = ttk.Label(text='Нарисуйте цифру', font=("Helvetica", 16))
# text.place(x=CANVAS_WIDTH // 2 - 40, y=CANVAS_HEIGHT // 2 - 50)
text_title = tk.Label(root, text="NUMBER RECOGNIZER", font=("Impact", 30), bg="#358abf", fg='#0f3753')
text_title.place(x=HEIGHT // 2, y=5)

# Запускаем главный цикл обработки событий
root.mainloop()
