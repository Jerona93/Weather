from tkinter import *
from tkmacosx import Button #This is only in MacOs, for buttons
import requests # To establish connection with the api

#-----------Window

root = Tk()
root.title('The Real Weather')
root.geometry('720x400')
root.configure(background='#E3FBF7')

entrada = StringVar()
def printinput(*args):
    print(entrada.get())
entrada.trace("w", printinput)

e = Entry(root, width=40, textvariable=entrada, highlightbackground = "#E3FBF7")
e.pack(pady=20)
e.insert(0, " ")

count = 0 # Try's count

def click():
    city = entrada.get()
    # conection with api
    api_key = 'ab330cff9f93cc2735e3342473038b18'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    data = requests.get(url)

    #conexion = str(data.status_code)
    temp = data.json()['main']['temp']
    tempmin = data.json()['main']['temp_min']
    tempmax = data.json()['main']['temp_max']
    weather = data.json()['weather'][0]['main']

    global count
    count += 1

    if count <= 3:
        cuenta.config(text=f'you have made {count} searches')
        
        if data.status_code == 200:

            frame = LabelFrame(root, text=city, padx=20, pady=10, borderwidth=0) 
            frame.pack(side=LEFT, padx=30, pady=10)
            frame.configure(background='#E3FBF7')

            l1 = Label(frame, text="Weather: " + weather)
            l1.configure(background='#E3FBF7')
            l1.pack()
            temperature = Label(frame, text= "Temperatura: "+str(temp))
            temperature.configure(background='#E3FBF7')
            temperature.pack()
            tempmin = Label(frame, text= "Temp min: "+str(tempmin))
            tempmin.configure(background='#E3FBF7')
            tempmin.pack()
            tempmax = Label(frame, text= "Temp max: "+str(tempmax))
            tempmax.configure(background='#E3FBF7')
            tempmax.pack()
            
        else:
            error = Label(frame, text="Introduce una ciudad correcta")
            error.pack()

    if count == 3: 
        btn.pack_forget()
        btn2 = Button(root, text='Clear')
        btn2.pack(side=LEFT, padx=30, pady=10)
    


cuenta = Label(root, text='Can you search 3 cities')
cuenta.configure(background='#E3FBF7')
cuenta.pack()

btn = Button(root, text='Search', command=click, highlightbackground = "#E3FBF7")
btn.pack()



root.bind('<Return>', lambda event=None: btn.invoke())  # link button with "enter" key

root.mainloop()
