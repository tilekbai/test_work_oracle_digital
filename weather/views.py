import requests
from django.http import JsonResponse
from django.utils import timezone
from rest_framework.decorators import api_view
from django.http import JsonResponse
import config

LAST_REQUESTS = {}

@api_view(['GET'])
def get_weather(request):
    city_name = request.GET.get('city', '')
    if not city_name:
        return JsonResponse({'error': 'City name is required'}, status=400)

    current_time = timezone.now()
    last_request_time = LAST_REQUESTS.get(city_name)

    if last_request_time and (current_time - last_request_time).seconds < 1800:
        cached_data = LAST_REQUESTS[city_name]['data']
    else:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={config.api_key}&units=metric'
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return JsonResponse({'error': 'Failed to fetch weather data'}, status=response.status_code)

        LAST_REQUESTS[city_name] = {'time': current_time, 'data': data}
        cached_data = data

    weather_data = {
        'temperature': cached_data['main']['temp'],
        'pressure': cached_data['main']['pressure'],
        'wind_speed': cached_data['wind']['speed'],
    }

    return JsonResponse(weather_data)
