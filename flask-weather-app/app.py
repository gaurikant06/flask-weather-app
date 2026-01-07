import requests
from flask import Flask, request, render_template

app = Flask(__name__)

def get_weather(city):
    API_KEY = "Your_API_KEY_HERE"
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(URL)
    return response.json()


@app.route('/', methods = ["GET","POST"])
def hello():
    weather = None
    error = None
    if request.method == "POST":
        city = request.form["city"]
        data = get_weather(city)

        if data and str(data.get("cod")) == "200":
            weather = {
                "temp": data['main'] ['temp'],
                "condition": data['weather'][0]['description']
            }
        else:
            error = " City not found"

            
    return render_template("index.html",weather=weather, error=error)



if __name__ == '__main__':

    app.run(debug = True, port=8000)
