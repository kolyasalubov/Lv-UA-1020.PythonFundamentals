import tkinter as tk
import config
from tkinter import font
from my_OWM import weather_data

HEIGHT = 400
WIDTH = 550

def get_weather(place_f):
    # set labels variables from obtained weather
    global wind
    global clouds
    global humidity
    global temperature
    global rain
    global current_place
    global logo
    global logo1

    current_place.set('Current weather in '+place_f)
    w = weather_data(place_f)
    wind.set('Wind ' + str(w.wind()['speed'])+' m/s'+'      Wind gusts '+str(w.wind()['gust'])+' m/s')
    clouds.set('Current state: ' + str(w.detailed_status))
    humidity.set('Humidity           ' + str(w.humidity) + ' %')
    temperature.set('Temperature '+str(w.temperature('celsius')['temp'])+ ' '+ chr(176)+'C'
                    +'   Real Feel'+str(w.temperature('celsius')['feels_like'])+' '+ chr(176)+'C')
 #   rain.set('Precipitation          '+ str(w.rain))

    logo = tk.PhotoImage(file=image_selection(str(w.detailed_status)))
    logo1.config(image=logo, bg="light blue3")
    return

def image_selection(cloud_inp) -> str:
    match cloud_inp:
        case 'clear':
            return str(config.list_of_images[0])
        case 'light rain':
            return str(config.list_of_images[1])
        case 'storm':
            return str(config.list_of_images[2])
        case 'overcast clouds':
            return str(config.list_of_images[3])
        case 'broken clouds':
            return str(config.list_of_images[3])
        case 'rain':
            return str(config.list_of_images[4])
        case _:
            return str(config.list_of_images[0])
    


root = tk.Tk()
wind = tk.StringVar()
clouds = tk.StringVar()
current_place = tk.StringVar()
temperature = tk.StringVar()
rain = tk.StringVar()
humidity = tk.StringVar()
temp_feel = tk.StringVar()
# canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
# root.title("Weather Application")
# canvas.pack()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='light blue3')
root.title("Weather Application")
canvas.pack()

logo = tk.PhotoImage(file='sunny.png')
logo1 = tk.Label(image=logo, bg="light blue3")
logo1.place(relx=1, rely=0.1, relwidth=0.15, relheight=0.15, anchor='e')

frame = tk.Frame(root, bg="light blue", bd=5)
frame.place(relx=0.5, rely=1, relwidth=0.75, relheight=0.1, anchor='s')

entry_field = tk.Entry(frame, font=('Courier', 12), bg = 'white')
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="steel blue4", fg="white", 
                   font=('Calibry', 8), 
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

label_place = tk.Label(font=('Calibry', 18, 'bold'), textvariable=current_place, bg='light blue3')
label_place.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.1, anchor='c')

lower_frame = tk.Frame(root, bg='light blue', bd=10)
lower_frame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.7, anchor='n')

lower_frame = tk.Frame(root, bg='light blue', bd=10)
lower_frame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.7, anchor='n')

label_temp = tk.Label(lower_frame, font=('Calibry', 12), textvariable=temperature, bg='deep sky blue4')
label_temp.place(relx=0, rely=0, relwidth=1, relheight=0.2)

label_wind = tk.Label(lower_frame, font=('Calibry', 12), textvariable=wind, bg='deep sky blue4')
label_wind.place(relx=0, rely=0.2, relwidth=1, relheight=0.2)

label_rain = tk.Label(lower_frame, font=('Calibry', 12), textvariable=rain, bg='deep sky blue4')
label_rain.place(relx=0, rely=0.4, relwidth=1, relheight=0.2)

label_humidity = tk.Label(lower_frame, font=('Calibry', 12), textvariable=humidity, bg='deep sky blue4')
label_humidity.place(relx=0, rely=0.6, relwidth=1, relheight=0.2)

label_clouds = tk.Label(lower_frame, font=('Calibry', 12), textvariable=clouds, bg='deep sky blue4')
label_clouds.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)



root.mainloop()