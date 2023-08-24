# Project-3

## NimbusNow
Step into a world of instant weather wonders with NimbusNow! Whether you're planning a weekend getaway or simply want to know if you need an umbrella for your morning coffee run, NimbusNow has got you covered. With a playful interface and lightning-fast updates, you'll discover the joy of weather forecasts that are as thrilling as they are accurate. Rain or shine, embark on a weather adventure with NimbusNow!

## Api
[OpenWeatherAPI](https://openweathermap.org/api)

## ERDs
We will design the following entities:

* User: Stores user authentication and preferences.
* Location: Stores user-selected locations for weather updates.
* WeatherData: Stores the retrieved weather information for each location.

## Restful Routing Chart
+---------------------------------+-------------------------+--------------------------+
|           Endpoint              |        Description      |         Actions          |
+---------------------------------+-------------------------+--------------------------+
|   /                             | Home page               | GET                      |
|   /login/                       | User login              | GET, POST                |
|   /logout/                      | User logout             | POST (logout)            |
|   /profile/                     | User profile            | GET, POST, PUT, DELETE   |
|                                   and settings                                       |
|   /locations/                   | List of user's          | GET, POST                |
|                                   saved locations                                    |
|   /locations/<int:location_id>/ | Location details        | GET, PUT,DELETE          |
|   /locations/add/               | Add new location        | GET, POST                |
+---------------------------------+----------------------------------------------------+


## Wireframes of Use views

* 1.HomePage -
![Home-Page](Home-page.jpeg)

* 2.Welcom Screen -
![Welcome-Screen](Welcom-Page.jpeg)

## User Stories
* As a user, I want to view the current weather for my selected locations.
* As a user, I want to add new locations to track their weather.
* As a user, I want to see detailed weather information for each location.
* As a user, I want to manage my profile settings and preferences.

## MVP Goals
* Create a Django project with necessary configurations.
* Implement user authentication and registration.
* Develop a home page to display user's saved locations and basic weather information.
* Integrate the OpenWeather API to fetch weather data based on user-selected locations.
* Design a form to add new locations for weather updates.
* Build a location detail page to show comprehensive weather data.

## Stretch Goals
* Provide data visualization, such as graphs, to display historical weather trends.
* Implement user settings for temperature units (Celsius/Fahrenheit) and time formats.
* Incorporate real-time weather map using external libraries or APIs.
* Create a responsive design for mobile devices.