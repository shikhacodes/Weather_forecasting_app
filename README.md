# 	:ringed_planet: Weather_forecasting_app

### :muscle: Here is the final result:
![demo weather](https://user-images.githubusercontent.com/64718956/214505878-18c23c3c-2af3-4f8b-9468-7e884c347d9e.JPG)

### :warning: This project has been developed taking reference from youtube channel of Parvat Computer technology and is only meant for learning purpose as this app uses Open Weather API which incurs certain cost whenever a search is made, hence, the original API key has been replaced with the current one. It is suggested to signup at "https://openweathermap.org/" for generating your own API key for use. Reference video link: "https://www.youtube.com/watch?v=YbNWzyW_QF8&t=1088s"

## :gift: Introduction:

This desktop App let's the user to find weather reports such as temperature, humidity, pressure, wind speed and description etc. of any place in the world. You need to provide the name of a place. Not only this you will also get current time of that place. 

It fetches data for 8 days of weather forecast for any place inserted by the user in search bar. It is desigend in such way that user is able to find weather report of complete week (7 upcoming days ). 

## :man_technologist: Steps to clone this repository:

* For Git Bash:
  * Go to any location , right click => open git bash here. Write Command:- git clone https://github.com/shikhacodes/Weather_forecasting_app.git

## :gear: Requirements:

* Python version 3.8.10 must be installed on your system.
* Open command prompt and install the following libraries using below commands:
```
pip install tk
pip install geopy
pip install timezonefinder
pip install pytz
pip install requests
pip install pillow
```
* Replace the existing API key with your generated API key at Line 36 in weather.py:
  * Replace the existing API key( **appid=7ef98f0315a2e31567cff27b13a5e9f3** ) in below code line with your new generated API key: 
```
api="https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=7ef98f0315a2e31567cff27b13a5e9f3"
```
   
* Run weather.py file.


  
