from flask import Flask, render_template, request, jsonify
from api.weather_api import get_weather_data
from utils.map_click_handler import get_city_from_coordinates

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    data = request.json
    if 'city' in data:
        city = data['city']
        weather_data = get_weather_data(city)
    elif 'coordinates' in data:
        coordinates = data['coordinates']
        city = get_city_from_coordinates(coordinates)
        weather_data = get_weather_data(city)
    else:
        return jsonify({'error': 'Invalid request'}), 400

    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)