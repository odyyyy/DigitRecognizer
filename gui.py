import tkinter as tk
from PIL import Image, ImageDraw
import main


# Получаем координаты курсора мыши и реализуем рисование
def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill="black", width=15)
    draw.line([x1, y1, x2, y2], fill='black', width=15)


# Сохранение нарисованной цифры в jpg файл
def save_image():
    FILENAME = 'image.jpg'
    img.save(FILENAME)

    # Размещения текста о результатах предикта нейронной сети
    text_result = tk.Label(root, text=f'{main.recognize()[0]}', font=("Arial Black", 120), bg="#04819E", fg='#0f3753')
    text_result.place(x=CANVAS_WIDTH * 2 + 25, y=CANVAS_HEIGHT // 2)

    text_percent = tk.Label(root, text=f'{main.recognize()[1]}%', font=("Arial", 30), bg="#04819E", fg='#0f3753')
    text_percent.place(x=CANVAS_WIDTH * 2 + 46, y=HEIGHT - 200)

# Очистка холста
def clear():
    canvas.delete(tk.ALL)
    draw.rectangle((0, 0, img.size[0], img.size[1]), fill=(255, 255, 255))


# Создаем окно приложения
root = tk.Tk()

# Размер окна приложения
WIDTH = 900
HEIGHT = 600

root.geometry(f"{WIDTH}x{HEIGHT}+0+0")  # установка размера окна приложения с координатами (0,0) в левом верхнем углу
root.resizable(False, False)
root.title("Digit recognizer")

# Установка размеров фреймов и их размещение

frame_left = tk.Frame(root, bg="#04819E", width=WIDTH // 2 - 10, height=HEIGHT - 100)
frame_right = tk.Frame(root, bg="#04819E", width=WIDTH // 2 - 10, height=HEIGHT - 100)
frame_top = tk.Frame(root, bg="#38B2CE", width=WIDTH, height=70)

frame_left.pack(side='left', padx=0)
frame_right.pack(side='right', padx=0)
frame_top.place(x=0, y=0)

# Установка цвета заднего фона
root.config(bg="#03677F")

# Размер холста и другие константы
CANVAS_WIDTH = 300
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
clear_button = tk.Button(root, text="Очистить", command=clear, bg="#38B2CE",
                         fg="black", font=("Helvetica", 16), relief='flat')
guess_button = tk.Button(root, text="Распознать", command=save_image, bg="#38B2CE",
                         fg="black", font=("Helvetica", 16), relief='flat')

clear_button.place(x=CANVAS_WIDTH // 2 + 15, y=HEIGHT - 120)
guess_button.place(x=CANVAS_WIDTH * 2 + 10, y=HEIGHT - 120)

# Добавление текста
text_title = tk.Label(root, text="DIGIT RECOGNIZER", font=("Impact", 30), bg="#38B2CE", fg='#0f3753')
text_title.place(x=HEIGHT // 2, y=5)

text_res = tk.Label(root, text='Результат:', font=("Arial Black", 20), bg="#38B2CE", fg='#0f3753')
text_res.place(x=CANVAS_WIDTH * 2 - 5, y=CANVAS_HEIGHT // 2 - 50)


# Запускаем главный цикл обработки событий
root.mainloop()
