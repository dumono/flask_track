from flask import Flask
from weather import weather_by_city

app = Flask(__name__)

@app.route('/')
def index():
    weather = weather_by_city("Moscow, Russia")
    weather = False
    if weather:
        return f"Сейчас {weather['temp_C']}," \
           f"ощущается как {weather['FeelsLikeC']}"
    else:
        return "Прогноз сейчас недоступен"


if __name__ == "__main__":
    app.run(debug =True)