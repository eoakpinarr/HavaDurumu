from tkinter import *
from PIL import ImageTk, Image
import requests

url = 'https://api.openweathermap.org/data/2.5/weather'
api_key = 'f4141dddf290d16df3d6f3a635806070'
iconUrl = 'https://openweathermap.org/img/wn/{}@2x.png'

def getWeather(city):
    params = {'q': city, 'appid': api_key, 'lang': 'tr'}
    data = requests.get(url, params = params).json()
    if data:
        city = data['name'].capitalize()
        country = data['sys']['country']
        temp = int(data['main']['temp'] - 273.15)
        icon = data['weather'][0]['icon']
        condition = data['weather'][0]['description']
        return (city, country, temp, icon, condition)

def main():
    city = cityEntry.get()
    weather = getWeather(city)
    if weather:
        locationLabel['text'] = '{}{}'.format(weather[0], weather[1])
        tempLabel['text'] = '{}°C'.format(weather[2])
        conditionLabel['text'] = weather[4]
        icon = ImageTk.PhotoImage(Image.open(requests.get(iconUrl.format(weather[3]), stream=True).raw))
        iconLabel.configure(image=icon)
        iconLabel.image = icon

app = Tk()
app.geometry('300x450')
app.title('EOA Hava Durumu')

cityEntry = Entry(app, justify='center')
cityEntry.pack(fill=BOTH, ipady=10, padx=19, pady=5)
cityEntry.focus()

searchButton = Button(app,text='Arama', font=('Arial', 15), command=main)
searchButton.pack(fill=BOTH, ipady=10, padx=20)

iconLabel = Label(app)
iconLabel.pack()

locationLabel = Label(app, font=('Arial', 40))
locationLabel.pack()

tempLabel = Label(app, font=('Arial', 50, 'bold'))
tempLabel.pack()

conditionLabel = Label(app, font=('Arial', 20))
conditionLabel.pack()

app.mainloop()