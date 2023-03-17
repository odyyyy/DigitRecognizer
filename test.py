import tkinter as tk


class DrawingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Drawing App")
        self.master.geometry("900x600")

        # Добавляем изображение фона
        self.background_image = tk.PhotoImage(file="bg.png")
        self.background_label = tk.Label(self.master, image=self.background_image)
        self.background_label.place(x=0, y=0)

        # Создаем холст
        self.canvas = tk.Canvas(self.master, width=600, height=600, bg="white")
        self.canvas.place(x=150, y=0)

        # Создаем кнопку "Очистить"
        self.clear_button = tk.Button(self.master, text="Очистить", bg="#FF4136", fg="white", font=("Helvetica", 16),
                                      command=self.clear_canvas)
        self.clear_button.place(x=50, y=550, width=100, height=40)

        # Связываем события мыши с холстом
        self.canvas.bind("<ButtonPress-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

        self.is_drawing = False
        self.last_x, self.last_y = None, None

    def start_draw(self, event):
        self.is_drawing = True
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        if self.is_drawing:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, width=3)
            self.last_x, self.last_y = event.x, event.y

    def stop_draw(self, event):
        self.is_drawing = False

    def clear_canvas(self):
        self.canvas.delete("all")


if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
