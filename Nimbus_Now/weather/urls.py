from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name= "index"),
    path('save_weather_data/', views.save_weather_data, name='save_weather_data'),

    
]