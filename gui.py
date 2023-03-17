import tkinter as tk
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

root.geometry(f"{WIDTH}x{HEIGHT}+0+0")
root.resizable(False, False)

root.title("Number recognizer")

CANVAS_WIDTH = 300  # Ширина полотна
CANVAS_HEIGHT = 300
WHITE = (255, 255, 255)
RESIZE = (28, 28)

# Создаем холст для рисования
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")

# Привязываем обработчики событий мыши к холсту
canvas.bind("<B1-Motion>", paint)

# Отображаем холст
canvas.pack(side='left', padx=50)

# Копия холста на которую сохраняется нарисованная цифра
img = Image.new('RGB', (CANVAS_WIDTH, CANVAS_HEIGHT), WHITE)
draw = ImageDraw.Draw(img)

# Создаем, отображаем и настраиваем положение кнопок
clear_button = tk.Button(root, text="Очистить", command=clear, bg="#FF4136", fg="black", font=("Helvetica", 16))
guess_button = tk.Button(root, text="Распознать", command=save_image, bg="#44944A", fg="black", font=("Helvetica", 16))

clear_button.configure(font=("Arial", 16))
guess_button.configure(font=("Arial", 16))
clear_button.place(x=CANVAS_WIDTH / 2, y=HEIGHT-100)
guess_button.place(x=CANVAS_WIDTH * 2, y=HEIGHT-100)

# Устанавливаем задний фон
root.config(bg="#e9f5dc")
# canvas.create_image(0, 0, anchor="nw", image=background)
# background_label = tk.Label(background)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Запускаем главный цикл обработки событий
root.mainloop()
