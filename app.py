from flask import Flask, render_template, request
import requests

app = Flask(_name_)

# Replace with your OpenWeather API Key
API_KEY = "760614782cbd2951e566822a23c0a9ab"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            }
            response = requests.get(BASE_URL, params=params)
            data = response.json()

            if data.get("cod") == 200:
                weather_data = {
                    "city": city.title(),
                    "temperature": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "description": data["weather"][0]["description"].capitalize()
                }
            else:
                weather_data = {"error": "City not found!"}
    return render_template("index.html", weather=weather_data)

if _name_ == "_main_":
    app.run(debug=True)
