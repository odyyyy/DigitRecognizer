# import tkinter as tk
#
#
# class DrawingApp:
#     def __init__(self, master):
#         master = master
#         master.title("Drawing App")
#         master.geometry("900x600")
#
#         # Добавляем изображение фона
#         background_image = tk.PhotoImage(file="bg.png")
#         background_label = tk.Label(master, image=background_image)
#         background_label.place(x=0, y=0)
#
#         # Создаем холст
#         canvas = tk.Canvas(master, width=600, height=600, bg="white")
#         canvas.place(x=150, y=0)
#
#         # Создаем кнопку "Очистить"
#         clear_button = tk.Button(master, text="Очистить", bg="#FF4136", fg="white", font=("Helvetica", 16),
#                                       command=clear_canvas)
#         clear_button.place(x=50, y=550, width=100, height=40)
#
#         # Связываем события мыши с холстом
#         canvas.bind("<ButtonPress-1>", start_draw)
#         canvas.bind("<B1-Motion>", draw)
#         canvas.bind("<ButtonRelease-1>", stop_draw)
#
#         is_drawing = False
#         last_x, last_y = None, None
#
#     def start_draw(self, event):
#         is_drawing = True
#         last_x, last_y = event.x, event.y
#
#     def draw(self, event):
#         if is_drawing:
#             canvas.create_line(last_x, last_y, event.x, event.y, width=3)
#             last_x, last_y = event.x, event.y
#
#     def stop_draw(self, event):
#         is_drawing = False
#
#     def clear_canvas(self):
#         canvas.delete("all")
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = DrawingApp(root)
#     root.mainloop()
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw


# Получаем координаты курсора мыши и реализуем рисование
def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill="black", width=10)
    draw.line([x1, y1, x2, y2], fill='black', width=10)


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

# Установка заднего фона
# background = tk.PhotoImage(file="bg1.png")
# background_label = tk.Label(root, image=background)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.config(bg="#AABAF2") # Установка цвета заднего фона

CANVAS_WIDTH = 300  # Ширина полотна
CANVAS_HEIGHT = 300
WHITE = (255, 255, 255)
RESIZE = (28, 28)

# Создаем рамку
canvas_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
canvas_frame.place(x=50, y=50, width=400, height=500)

# Создаем холст внутри рамки
canvas = tk.Canvas(canvas_frame, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")

# Привязываем обработчики событий мыши к холсту
canvas.bind("<B1-Motion>", paint)

# Копия холста на которую сохраняется нарисованная цифра
img = Image.new('RGB', (CANVAS_WIDTH, CANVAS_HEIGHT), WHITE)
draw = ImageDraw.Draw(img)

# Создаем, отображаем и настраиваем положение кнопок
button_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
button_frame.place(x=500, y=50, width=400, height=500)
clear_button = tk.Button(button_frame, text="Очистить", command=clear, bg="#FF4136", fg="black", font=("Helvetica", 16))
guess_button = tk.Button(button_frame, text="Распознать", command=save_image, bg="#44944A", fg="black", font=("Helvetica", 16))

clear_button.place(x=CANVAS_WIDTH / 2, y=HEIGHT - 100)
guess_button.place(x=CANVAS_WIDTH * 2, y=HEIGHT - 100)

text = ttk.Label(text='Нарисуйте цифру', font=("Helvetica", 16))
text.place(x=CANVAS_WIDTH // 2 - 40, y=CANVAS_HEIGHT // 2 - 50)

# Запускаем главный цикл обработки событий
root.mainloop()
