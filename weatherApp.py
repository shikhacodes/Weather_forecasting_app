from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim 
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root= Tk()
root.title("Weather Forecasting App")
root.geometry("890x470+50+50")
root.configure(bg = "#57adff")
root.resizable(False, False)


def getWeather():
    city = textfield.get()

    geolocator= Nominatim(user_agent = "geoapiExercises")
    location=geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat= location.latitude)

    timezone.config(text = result)
    long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    #weather
    api="https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=646824f2b7b86caffec1d0b16ea77f79"
    json_data = requests.get(api).json()

    #current
    temp=json_data['current']['temp']
    #print(temp)
    humidity=json_data['current']['humidity']
    #print(humidity)
    pressure=json_data['current']['pressure']
    #print(pressure)
    wind=json_data['current']['wind_speed']
    #print(wind)
    description=json_data['current']['weather'][0]['description']
    #print(description)


    t.config(text=(temp,"°C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hPa"))
    w.config(text=(wind,"m/s"))
    d.config(text=description)


    #first cell
    firstdayimage= json_data['daily'][0]['weather'][0]['icon']
    photo1 = ImageTk.PhotoImage(file=f"Icon/{firstdayimage}@2x.png")
    firstimage.config(image=photo1)
    firstimage.image=photo1

    tempday1 = json_data['daily'][0]['temp']['day']
    tempnight1 = json_data['daily'][0]['temp']['night']

    day1temp.config(text=f"Day:{tempday1}°C\nNight:{tempnight1}°C")

    #second cell
    seconddayimage= json_data['daily'][1]['weather'][0]['icon']

    img=(Image.open(f"Icon/{seconddayimage}@2x.png"))
    resized_image= img.resize((50,50))
    photo2= ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image=photo2

    tempday2 = json_data['daily'][1]['temp']['day']
    tempnight2 = json_data['daily'][1]['temp']['night']

    day2temp.config(text=f"D: {tempday2}°C\nN: {tempnight2}°C")
    day2temp.place(x=3,y=70)

    #third cell
    thirddayimage= json_data['daily'][2]['weather'][0]['icon']

    img=(Image.open(f"Icon/{thirddayimage}@2x.png"))
    resized_image= img.resize((50,50))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image=photo3

    tempday3 = json_data['daily'][2]['temp']['day']
    tempnight3 = json_data['daily'][2]['temp']['night']

    day3temp.config(text=f"D: {tempday3}°C\nN: {tempnight3}°C")
    day3temp.place(x=3,y=70)

    #fourth cell
    fourthdayimage= json_data['daily'][3]['weather'][0]['icon']

    img=(Image.open(f"Icon/{fourthdayimage}@2x.png"))
    resized_image= img.resize((50,50))
    photo4= ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image=photo4

    tempday4 = json_data['daily'][3]['temp']['day']
    tempnight4 = json_data['daily'][3]['temp']['night']

    day4temp.config(text=f"D: {tempday4}°C\nN: {tempnight4}°C")
    day4temp.place(x=3,y=70)

    #fifth cell
    fifthdayimage= json_data['daily'][4]['weather'][0]['icon']
    
    img=(Image.open(f"Icon/{fifthdayimage}@2x.png"))
    resized_image= img.resize((50,50))
    photo5= ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image=photo5

    tempday5 = json_data['daily'][4]['temp']['day']
    tempnight5 = json_data['daily'][4]['temp']['night']

    day5temp.config(text=f"D: {tempday5}°C\nN: {tempnight5}°C")
    day5temp.place(x=3,y=70)

    #sixth cell
    sixthdayimage= json_data['daily'][5]['weather'][0]['icon']

    img=(Image.open(f"Icon/{sixthdayimage}@2x.png"))
    resized_image= img.resize((50,50))
    photo6= ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image=photo6

    tempday6 = json_data['daily'][5]['temp']['day']
    tempnight6 = json_data['daily'][5]['temp']['night']

    day6temp.config(text=f"D: {tempday6}°C\nN: {tempnight6}°C")
    day6temp.place(x=3,y=70)

    #seventh cell
    seventhdayimage= json_data['daily'][6]['weather'][0]['icon']

    img=(Image.open(f"Icon/{seventhdayimage}@2x.png"))
    resized_image= img.resize((50,50))
    photo7= ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image=photo7

    tempday7 = json_data['daily'][6]['temp']['day']
    tempnight7 = json_data['daily'][6]['temp']['night']

    day7temp.config(text=f"D: {tempday7}°C\n N: {tempnight7}°C")
    day7temp.place(x=3,y=70)
    
    #days

    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first+timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first+timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first+timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))

    

##icon
image_icon = PhotoImage(file = "Images\logo.png")
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file = "Images\Rounded Rectangle 1.png")


Label(root, image = Round_box, bg= "#57adff").place(x=25, y=110)

#label
label1 = Label(root, text = "Temperature", font=('Helvetica', 11), fg="white", bg="#202f43")
label1.place(x=33, y = 120)

label2 = Label(root, text = "Humidity", font=('Helvetica', 11), fg="white", bg="#202f43")
label2.place(x=33, y = 140)

label3 = Label(root, text = "Pressure", font=('Helvetica', 11), fg="white", bg="#202f43")
label3.place(x=33, y = 160)

label4 = Label(root, text = "Wind speed", font=('Helvetica', 11), fg="white", bg="#202f43")
label4.place(x=33, y=180)

label5 = Label(root, text = "Description", font=('Helvetica', 11), fg="white", bg="#202f43")
label5.place(x=33, y = 200)


#search bar
Search_image = PhotoImage(file = "Images/Rounded Rectangle 3.png")
myimage = Label(image = Search_image, bg="#57adff" )
myimage.place( x=270 ,y=100)

weat_image = PhotoImage(file = "Images/cloud.png")
weatherimage= Label(root, image= weat_image, bg="#202f43")
weatherimage.place(x=289, y=105)

textfield = tk.Entry(root, justify = "center", width = 15, font = ("poppins", 25, "bold"), bg = "#202f43", border = 0, fg = "white")
textfield.place(x = 380, y = 112)
textfield.focus()

Search_icon = PhotoImage("Images/Layer 6.png")
myimage_icon =Button(image = Search_icon, borderwidth = 10, cursor = "hand2", bg = "#202f43",command= getWeather)
myimage_icon.place(x = 645, y = 120)

#bottom box
frame = Frame(root, width = 900, height = 180, bg = "#212120")
frame.pack(side=BOTTOM)

#bottom boxes
firstbox = PhotoImage(file = "Images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file = "Images/Rounded Rectangle 2 copy.png")

Label(frame, image = firstbox, bg = "#212120").place(x = 30, y = 20)
Label(frame, image = secondbox, bg = "#212120").place(x= 295, y = 30)
Label(frame, image = secondbox, bg = "#212120").place(x= 395, y = 30)
Label(frame, image = secondbox, bg = "#212120").place(x= 495, y = 30)
Label(frame, image = secondbox, bg = "#212120").place(x= 595, y = 30)
Label(frame, image = secondbox, bg = "#212120").place(x= 695, y = 30)
Label(frame, image = secondbox, bg = "#212120").place(x= 795, y = 30)

#clock
clock = Label(root, font = ("Helvetica", 30 , 'bold'), fg = "white", bg = "#57adff")
clock.place(x = 50, y = 20)

#timezone
timezone = Label(root, font = ("Helvetica", 20 ), fg = "white", bg = "#57adff")
timezone.place(x = 700, y = 20)

long_lat = Label(root, font = ("Helvetica", 10 ), fg = "white", bg = "#57adff")
long_lat.place(x = 700, y = 50)

#thpwd
t = Label(root,font=('Helvetica',11),fg="white",bg="#203243")
t.place(x=150,y=120)
h = Label(root,font=('Helvetica',11),fg="white",bg="#203243")
h.place(x=150,y=140)
p = Label(root,font=('Helvetica',11),fg="white",bg="#203243")
p.place(x=150,y=160)
w = Label(root,font=('Helvetica',11),fg="white",bg="#203243")
w.place(x=150,y=180)
d = Label(root,font=('Helvetica',11),fg="white",bg="#203243")
d.place(x=150,y=200)

#first cell
firstframe=Frame(root,width=230,height=132,bg="#282829")
firstframe.place(x=35,y=315)

day1=Label(firstframe,font="arial 15",bg="#282829",fg="#fff")
day1.place(x=101,y=5)

firstimage=Label(firstframe,bg="#282829")
firstimage.place(x=1,y=15)

day1temp = Label(firstframe, bg="#282829", fg="#57adff", font= "arial 15 bold")
day1temp.place(x=100,y=50)

#second cell
secondframe=Frame(root,width=70,height=115,bg="#282829")
secondframe.place(x=301,y=325)

day2=Label(secondframe,bg="#282829",fg="#fff")
day2.place(x=3,y=3)

secondimage=Label(secondframe,bg="#282829")
secondimage.place(x=7,y=20)

day2temp = Label(secondframe, bg="#282829", fg="#57adff")
day2temp.place(x=10,y=70)



#third cell
thirdframe=Frame(root,width=70,height=115,bg="#282829")
thirdframe.place(x=401,y=325)

day3=Label(thirdframe,bg="#282829",fg="#fff")
day3.place(x=3,y=3)

thirdimage=Label(thirdframe,bg="#282829")
thirdimage.place(x=7,y=20)

day3temp = Label(thirdframe, bg="#282829", fg="#57adff")
day3temp.place(x=10,y=70)

#fourth cell
fourthframe=Frame(root,width=70,height=115,bg="#282829")
fourthframe.place(x=501,y=325)

day4=Label(fourthframe,bg="#282829",fg="#fff")
day4.place(x=3,y=3)

fourthimage=Label(fourthframe,bg="#282829")
fourthimage.place(x=7,y=20)

day4temp = Label(fourthframe, bg="#282829", fg="#57adff")
day4temp.place(x=10,y=70)

#fifth cell
fifthframe=Frame(root,width=70,height=115,bg="#282829")
fifthframe.place(x=601,y=325)

day5=Label(fifthframe,bg="#282829",fg="#fff")
day5.place(x=3,y=3)

fifthimage=Label(fifthframe,bg="#282829")
fifthimage.place(x=7,y=20)

day5temp = Label(fifthframe, bg="#282829", fg="#57adff")
day5temp.place(x=10,y=70)

#sixth cell
sixthframe=Frame(root,width=70,height=115,bg="#282829")
sixthframe.place(x=701,y=325)

day6=Label(sixthframe,bg="#282829",fg="#fff")
day6.place(x=3,y=3)

sixthimage=Label(sixthframe,bg="#282829")
sixthimage.place(x=7,y=20)

day6temp = Label(sixthframe, bg="#282829", fg="#57adff")
day6temp.place(x=10,y=70)

#seventh cell
seventhframe=Frame(root,width=70,height=115,bg="#282829")
seventhframe.place(x=801,y=325)

day7=Label(seventhframe,bg="#282829",fg="#fff")
day7.place(x=3,y=3)

seventhimage=Label(seventhframe,bg="#282829")
seventhimage.place(x=7,y=20)

day7temp = Label(seventhframe, bg="#282829", fg="#57adff")
day7temp.place(x=10,y=70)



root.mainloop()
