from tkinter import *
from tkinter import messagebox as tkMessageBox
from tkinter import ttk, colorchooser, filedialog
import PIL
from PIL import Image, ImageDraw, ImageGrab

class Paint3000(Frame):

    def __init__(self, master):
        
        Frame.__init__(self, master)
        self.master = master
        self.color = "black"
        self.brush_size = 7
        self.color2 = "white"
        self.lastik_size = 5
        self.GUI()
        self.color_fg = "black"
        self.old_x = None
        self.old_y = None
        
    def set_color(self, new_color):
        self.color = new_color
        
    def set_color2(self, new_color2):
        self.color2 = new_color2

    def set_brush_size(self, new_size):
        self.brush_size = new_size
        
    def set_lastik_size(self, new_lastik):
        self.lastik_size = new_lastik

    def change_fg(self): #палитра
        self.color=colorchooser.askcolor(color=self.color)[1]

    def draw(self, event): #рисовалка       
        if self.old_x and self.old_y:
            self.canv.create_line(self.old_x,self.old_y,event.x,event.y,width=self.brush_size,fill=self.color,capstyle=ROUND,smooth=True)

        self.old_x = event.x
        self.old_y = event.y
        
    def lastik(self, event):     
        if self.old_x and self.old_y:
            self.canv.create_line(self.old_x,self.old_y,event.x,event.y,width=self.lastik_size,fill=self.color2,capstyle=ROUND,smooth=True)

        self.old_x = event.x
        self.old_y = event.y

    def reset(self,event):
        self.old_x = None
        self.old_y = None

    def save(self): #сохранение
        file = filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics','*.png')])
        if file:
            x = self.master.winfo_rootx() + self.canv.winfo_x()
            y = self.master.winfo_rooty() + self.canv.winfo_y()
            x1 = x + self.canv.winfo_width()
            y1 = y + self.canv.winfo_height()

            PIL.ImageGrab.grab().crop((x,y,x1,y1)).save(file + '.png')

    def about(self): #це кнопки информации
        tkMessageBox.showinfo(title="О программе",message="Программа MadPaint3000 создана для курсовой работы. Не является графическим редактором.")

    def team(self):
        tkMessageBox.showinfo(title="Команда",message="Команда: Пантюхин Никита, Солодов Максим, Савицкий Егор")

    def howto(self):
        tkMessageBox.showinfo(title="MadPaint HELP",message="Для сохранения изображения нажмите 'Файл -> Сохранить как...'. Если количество предоставленных цветов Вас не устраивает, вы можете вызвать меню палитры цветов 'Цвета -> Палитра цветов'.")

    def GUI(self): #це интерфейс
       
        self.master.title("MadPaint3000")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(15, weight=2)
        self.rowconfigure(4, weight=1)

        self.canv = Canvas(self, bg="white")
        self.canv.grid(row=4, column=0, columnspan=25,
                       padx=5, pady=5, sticky=E+W+S+N)  # тут рабочее пространство
        
        self.canv.bind("<B1-Motion>", self.draw)
        self.canv.bind("<ButtonRelease-1>", self.reset)# рисовалка
        
        self.canv.bind("<B3-Motion>", self.lastik)
        self.canv.bind("<ButtonRelease-3>", self.reset)

        colorpanel = Label(self, text="Цвета: ") # ряд цветов
        colorpanel.grid(row=0, column=0, padx=6)

        red_btn = Button(self, background="red", width=2,
                         command=lambda: self.set_color("red"))
        red_btn.grid(row=0, column=1) 

        green_btn = Button(self,background="green", width=2,
                           command=lambda: self.set_color("green"))
        green_btn.grid(row=0, column=2)

        blue_btn = Button(self, background="blue", width=2,
                          command=lambda: self.set_color("blue"))
        blue_btn.grid(row=0, column=3)

        black_btn = Button(self,background="black", width=2,
                           command=lambda: self.set_color("black"))
        black_btn.grid(row=0, column=4)

        white_btn = Button(self,background="white", width=2,
                           command=lambda: self.set_color("white"))
        white_btn.grid(row=0, column=5)

        yellow_btn = Button(self,background="yellow", width=2,
                           command=lambda: self.set_color("yellow"))
        yellow_btn.grid(row=0, column=6,sticky=W)

        grey_btn = Button(self,background="grey", width=2,
                           command=lambda: self.set_color("grey"))
        grey_btn.grid(row=0, column=7,sticky=W)

        purple_btn = Button(self,background="purple", width=2,
                           command=lambda: self.set_color("purple"))
        purple_btn.grid(row=1, column=1,sticky=W)

        lightblue_btn = Button(self,background="lightblue", width=2,
                           command=lambda: self.set_color("lightblue"))
        lightblue_btn.grid(row=1, column=2,sticky=W)

        orange_btn = Button(self,background="orange", width=2,
                           command=lambda: self.set_color("orange"))
        orange_btn.grid(row=1, column=3,sticky=W)

        chartreuse_btn = Button(self,background="chartreuse", width=2,
                           command=lambda: self.set_color("chartreuse"))
        chartreuse_btn.grid(row=1, column=4,sticky=W)

        lightblue_btn = Button(self,background="lightblue", width=2,
                           command=lambda: self.set_color("lightblue"))
        lightblue_btn.grid(row=1, column=2,sticky=W)

        orange_btn = Button(self,background="orange", width=2,
                           command=lambda: self.set_color("orange"))
        orange_btn.grid(row=1, column=3,sticky=W)

        chartreuse_btn = Button(self,background="chartreuse", width=2,
                           command=lambda: self.set_color("chartreuse"))
        chartreuse_btn.grid(row=1, column=4,sticky=W)

        indigo_btn = Button(self,background="indigo", width=2,
                           command=lambda: self.set_color("indigo"))
        indigo_btn.grid(row=1, column=5,sticky=W)

        brown_btn = Button(self,background="brown", width=2,
                           command=lambda: self.set_color("brown"))
        brown_btn.grid(row=1, column=6,sticky=W)

        magenta_btn = Button(self,background="magenta", width=2,
                           command=lambda: self.set_color("magenta"))
        magenta_btn.grid(row=1, column=7,sticky=W)     

        toolpanel = Label(self, text="Инструменты: ") #инструменты
        toolpanel.grid(row=0, column=8, padx=6) # Устанавливаем созданную метку в первый ряд и первую колонку, задаем горизонтальный отступ в 6 пикселей


        lastik_btn = Button(self,text="Ластик", width=10,
                           command=lambda: self.set_color2("white"))
        lastik_btn.grid(row=0, column=9)

        clear_btn = Button(self, text="Очистить все", width=10,
                           command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=11)
        
        lastiksizepanel = Label(self, text="Размер ластика: ") #
        lastiksizepanel.grid(row=2, column=8, padx=6) #
        
        lastiksize = Button(self,text="5px", width=7,
                           command=lambda: self.set_lastik_size(5))
        lastiksize.grid(row=2, column=9)

        lastiksize2 = Button(self,text="7px", width=7,
                           command=lambda: self.set_lastik_size(7))
        lastiksize2.grid(row=2, column=10)

        lastiksize3 = Button(self,text="10px", width=7,
                           command=lambda: self.set_lastik_size(10))
        lastiksize3.grid(row=2, column=11)

        lastiksize4 = Button(self,text="20px", width=7,
                           command=lambda: self.set_lastik_size(20))
        lastiksize4.grid(row=2, column=12)

        panelkisti = Label(self, text="Размер кисти: ") # ряд кистей, выбор размера кисти
        panelkisti.grid(row=2, column=0, padx=0)
        one_btn = Button(self, text="2", width=2,
                         command=lambda: self.set_brush_size(2))
        one_btn.grid(row=2, column=1)

        two_btn = Button(self, text="5", width=2,
                         command=lambda: self.set_brush_size(5))
        two_btn.grid(row=2, column=2)

        five_btn = Button(self, text="7", width=2,
                          command=lambda: self.set_brush_size(7))
        five_btn.grid(row=2, column=3)

        seven_btn = Button(self, text="10", width=2,
                           command=lambda: self.set_brush_size(10))
        seven_btn.grid(row=2, column=4)

        ten_btn = Button(self, text="24", width=2,
                         command=lambda: self.set_brush_size(24))
        ten_btn.grid(row=2, column=5)

        twenty_btn = Button(self, text="48", width=2,
                            command=lambda: self.set_brush_size(48))
        twenty_btn.grid(row=2, column=6, sticky=W)

        menu = Menu(self.master) #менюха
        self.master.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='Файл',menu=filemenu)
        filemenu.add_command(label='Сохранить как...',command=self.save)
        colormenu = Menu(menu)
        menu.add_cascade(label='Цвета',menu=colormenu)
        colormenu.add_command(label='Палитра цветов',command=self.change_fg)
        optionmenu = Menu(menu)
        menu.add_cascade(label='Опции',menu=optionmenu)
        optionmenu.add_command(label='Очистить все',command=self.canv.delete("all"))
        helpmenu = Menu(menu)
        menu.add_cascade(label='Помощь',menu=helpmenu)
        helpmenu.add_command(label='О программе',command=self.about)
        helpmenu.add_command(label='Команда',command=self.team)
        helpmenu.add_command(label='MadPaint Help',command=self.howto)
        
        
def main(): #okno
    root = Tk()
    root.geometry("1024x768")
    app = Paint3000(root)
    root.mainloop()

if __name__ == '__main__':
    main()
