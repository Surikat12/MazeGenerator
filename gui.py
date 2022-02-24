from tkinter import *
import tkinter.ttk as ttk
from Maze import Maze
from tkinter import messagebox
from PIL import ImageTk, Image


maze = None
image = None
root = Tk()
root.title("Генерация лабиринтов")
root.geometry("1600x800")

frame = Frame(root, bd=1)
frame.place(x=0, y=0)
tab = ttk.Notebook(frame)
tab.grid(row=0, columnspan=2)

tab1 = ttk.Frame(tab)
tab2 = ttk.Frame(tab)
tab.add(tab1, text="Sidewinder")
tab.add(tab2, text="Hunt and Kill")

btn1 = Button(tab1, text="Генерировать")
btn1.grid(column=0)
btn2 = Button(tab2, text="Генерировать")
btn2.grid(column=0)


label1 = Label(frame, text="Высота:").grid(row=1, column=0)
label2 = Label(frame, text="Ширина:").grid(row=2, column=0)
text_h = Entry(frame)
text_h.grid(row=1, column=1)
text_w = Entry(frame)
text_w.grid(row=2, column=1)
btn_solve = Button(frame, text="Решить")
btn_solve.grid(row=3, column=0)

pic_frame = Frame(root, width=1000, height=1000)
pic_frame.place(x=250, y=0)

canvas = Canvas(pic_frame, width=960, height=960)
canvas.grid(row=0, column=0)


def canvas_update(name):
    global image
    try:
        image_ = Image.open(name)
        if image_.width == image_.height or image_.width > 750 or image_.height > 750:
            image_ = image_.resize((750, 750))
        image = ImageTk.PhotoImage(image_)
        canvas.create_image(1, 1, image=image, anchor='nw')
    except FileNotFoundError:
        print("Файл не найден")


def generate_sidewinder(event):
    try:
        global maze
        height = int(text_h.get())
        width = int(text_w.get())
        maze = Maze(height, width)
        maze.generate_maze_sidewinder()
        maze.draw_maze()
        canvas_update("Maze.png")
    except ValueError:
        messagebox.showerror("Ошибка", "В полях должны находится целые числа большие нуля")
    except IndexError:
        messagebox.showerror("Ошибка", "В полях должны находится целые числа большие нуля. Индексы")


def generate_hak(event):
    try:
        global maze
        height = int(text_h.get())
        width = int(text_w.get())
        maze = Maze(height, width)
        maze.generate_maze_hunt_and_kill()
        maze.draw_maze()
        canvas_update("Maze.png")
    except ValueError:
        messagebox.showerror("Ошибка", "В полях должны находится целые числа большие нуля")
    except IndexError:
        messagebox.showerror("Ошибка", "В полях должны находится целые числа большие нуля. Индексы")


def solve_and_draw(event):
    try:
        global maze
        maze.solve()
        maze.solve_draw()
        canvas_update("Solve_maze.png")
    except (FileNotFoundError, IndexError, ValueError, AttributeError):
        messagebox.showerror("Ошибка", "Лабиринт не создан")


btn1.bind("<Button-1>", generate_sidewinder)
btn2.bind("<Button-1>", generate_hak)
btn_solve.bind("<Button-1>", solve_and_draw)
root.mainloop()
