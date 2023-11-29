from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from flask import Flask, jsonify
from .models import WeatherHistory
from cloud_to_go import api_token

# Create your views here.
app = Flask(__name__)

@app.route('/api/weather/<string:city>/', methods=['GET'])
@csrf_exempt
def get_weather(request, city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid=f8d93f917d7685ab2268c4296a329c51&lang=pt_BR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        WeatherHistory.objects.create(city=city)
        return jsonify(data)
    else:
        return jsonify({"error": f"Error: {response.status_code}"}), response.status_code
