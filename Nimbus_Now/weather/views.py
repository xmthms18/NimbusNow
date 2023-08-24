import datetime
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render #redirect
from django.contrib.auth.forms import UserCreationForm
from .models import SavedWeatherData
from django.http import JsonResponse


# Create your views here.
#def signup_view(request):
    #if request.method == 'POST':
       # form = UserCreationForm(request.POST)
       # if form.is_valid():
           # form.save()
            #return redirect('login')
    #else:
        #form = UserCreationForm()
    #return render(request, 'registration/signup.html', {'form': form})




def save_weather_data(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        temperature = float(request.POST.get('temperature'))
        description = request.POST.get('description')
        icon = request.POST.get('icon')

        # Save weather data for the current user
        SavedWeatherData.objects.create(
            user=request.user,
            city=city,
            temperature=temperature,
            description=description,
            icon=icon
        )

        return JsonResponse({'message': 'Weather data saved successfully.'})

    return JsonResponse({'message': 'Invalid request.'}, status=400)



#@login_required
def index(request):
    API_KEY = "ea176ef47b541be3c93f392589821086"
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial'
    forecast_url = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}&units=imperial'

    if request.method == 'POST':
        city1 = request.POST['city1']
        city2 = request.POST.get('city2', None)

        weather_data1, daily_forecasts1 = fetch_weather_and_forecast(city1, API_KEY, current_weather_url, forecast_url)

        if city2:
            weather_data2, daily_forecasts2 = fetch_weather_and_forecast(city2, API_KEY, current_weather_url,forecast_url)
        else:
            weather_data2, daily_forecasts2 = None, None

        context = {
            'weather_data1': weather_data1,
            'daily_forecasts1': daily_forecasts1,
            'weather_data2': weather_data2,
            'daily_forecasts2': daily_forecasts2,
        }

        return render(request, 'weather_app/index.html', context)
    
    else:
        return render(request, 'weather_app/index.html')
    
def fetch_weather_and_forecast(city, api_key, current_weather_url, forecast_url):
      response = requests.get(current_weather_url.format(city, api_key )).json()
      print("API response: ", response) # debugging

      if 'coord' in response:
          lat, lon = response['coord']['lat'], response['coord']['lon']
      else:
          print('The key "coord" was not found in the response')
          lat, lon = None, None

      if lat and lon:
          with requests.get(forecast_url.format(lat, lon, api_key)) as forecast_response:
              forecast_data = forecast_response.json()
      else:
          forecast_data = None

      weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'], 2),
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
      }
      
      daily_forecasts = []
      if forecast_data and 'daily' in forecast_data:
          for daily_data in forecast_data['daily'][:5]:
              daily_forecasts.append({
                  'day': datetime.datetime.fromtimestamp(daily_data['dt']).strftime('%A'),
                  'min_temp': round(daily_data['temp']['min'], 2),
                  'max_temp': round(daily_data['temp']['max'], 2),
                  'description': daily_data['weather'][0]['description'],
                  'icon': daily_data['weather'][0]['icon'],
              })

      return weather_data, daily_forecasts
