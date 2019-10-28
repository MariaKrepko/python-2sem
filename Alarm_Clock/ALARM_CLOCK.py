import tkinter, time, pyglet,winsound
from time import strftime
import tkinter.messagebox


#функции времени текущее время
def time():
    global check
    if check == 0:
        h=int(strftime('%H'))
        m=int(strftime('%M'))
        hours1.set(convert(h))
        minutes1.set(convert(int(strftime('%M'))))
        root.after(6000, time)

def time1():
    image_hours=tkinter.Label(width=15,height=9,fg = 'dark slate gray',bg= 'lightcyan',textvariable = hours)
    image_hours.grid(row=0,column=1)
    image_minutes = tkinter.Label(width=15,height=9,fg = 'dark slate gray',bg= 'lightcyan',textvariable = minutes)
    image_minutes.grid(row=0,column=3,columnspan=1)

    
#функция для конвертирования времени в нужный формат
def convert(n):
    if n < 9:
        return "0" + str(n)
    else:
        return str(n)

#Кнопка H увеличение часов
def increase_h():
    if int(hours.get()) < int(control_hours.get()) :
        if int(hours.get())< 9:
             hours.set('0'+str(int(hours.get()) + 1))
        else:
            hours.set(str(int(hours.get())+1))
    else:
        hours.set('00')
        
#Кнопка M увеличение минут
def increase_m():
    if int(minutes.get()) < int(control_minutes.get()) :
        if int(minutes.get()) < 9:
             minutes.set('0'+str(int(minutes.get()) + 1))
        else:
            minutes.set(str(int(minutes.get())+1))
    else:
        minutes.set('00')


        


#Кнопка А
def start():                 
    global check             
    if check==0:            
        time1()
        check +=1 
    elif check == 1:
        time()
        if int(hours.get()) == int(strftime('%H')) and int(minutes.get()) == int(strftime('%M')):
            check=0
            time1()

        elif int(hours.get()) <= int(strftime('%H')) and int(minutes.get()) <= int(strftime('%M')):
            tkinter.messagebox.showinfo('Warning', 'будильник не может быть установлен')
            check = 0
            time1()
                
        else:
            clock_time = int(strftime('%H')) * 3600 +int(strftime('%M'))*60+ int(strftime('%S'))
            alarm_time = int(hours.get()) * 3600 + int(minutes.get())*60
            tkinter.messagebox.showinfo('Alarm clock', 'будильник установлен')            
            root.after((alarm_time - clock_time ) * 1000, playsoung)
            
        check=0

#музыка
def playsoung () :
    sound = pyglet.media.load('SOUNG.wav')
    sound.play()
    pyglet.app.run()
    global cheak
    check=0
    time()
    
def stopsound ():
    pyglet.app.exit    
 

#Визуализация для настройки часов и минут будильника
root = tkinter.Tk()
root.title("Alarm Clock")
root.iconbitmap(default='alarm_clock_image.ico')
root.geometry('281x210')
root['bg']='light sea green'

hours1=tkinter.StringVar()
hours1.set(int(strftime('%H')))
minutes1=tkinter.StringVar()
minutes1.set(int(strftime('%M')))

hours=tkinter.StringVar()
hours.set('00')
minutes=tkinter.StringVar()
minutes.set('00')

control_hours=tkinter.StringVar()
control_hours.set(23)
control_minutes=tkinter.StringVar()
control_minutes.set(59)

check=0

none=tkinter.Label()
none['bg']='light sea green'
none.grid(row=0, column=0, rowspan=4)

image_hours=tkinter.Label(width=15,height=9,fg = 'dark slate gray',bg= 'lightcyan',textvariable = hours1)
image_hours.grid(row=0,column=1)

image_colon=tkinter.Label(width=6,height=9,bg= 'lightcyan',text=':')
image_colon.grid(row=0,column=2)

image_minutes = tkinter.Label(width=15,height=9,fg = 'dark slate gray',bg= 'lightcyan',textvariable = minutes1)
image_minutes.grid(row=0,column=3,columnspan=1)

none1=tkinter.Label()
none1['bg']='light sea green'
none1.grid(row=2, column=0, columnspan=4)

#кнопки H,M,A
hours_button=tkinter.Button(width=5,height=2,text='H', bg='lightcyan',command=increase_h)
hours_button.grid(row=3,column=1)

minutes_button=tkinter.Button(width=5,height=2,text='M',bg='lightcyan', command=increase_m)
minutes_button.grid(row=3,column=2)

alamr_button=tkinter.Button(width=5,height=2,text='A',bg='lightcyan',command=start)
alamr_button.grid(row=3,column=3)


root.mainloop()





