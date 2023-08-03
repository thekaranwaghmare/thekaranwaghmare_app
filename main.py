import requests

def get_weather_data():
    url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    data = response.json()
    return data

def get_weather_for_date(data, date):
    for forecast in data['list']:
        if date in forecast['dt_txt']:
            return forecast['main']['temp']
    return None

def get_wind_speed_for_date(data, date):
    for forecast in data['list']:
        if date in forecast['dt_txt']:
            return forecast['wind']['speed']
    return None

def get_pressure_for_date(data, date):
    for forecast in data['list']:
        if date in forecast['dt_txt']:
            return forecast['main']['pressure']
    return None

if _name_ == "_main_":
    data = get_weather_data()

    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            temp = get_weather_for_date(data, date)
            if temp:
                print(f"Temperature on {date}: {temp} K")
            else:
                print("Data not available for the given date.")
        elif choice == 2:
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            wind_speed = get_wind_speed_for_date(data, date)
            if wind_speed:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Data not available for the given date.")
        elif choice == 3:
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            pressure = get_pressure_for_date(data, date)
            if pressure:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Data not available for the given date.")
        elif choice == 0:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")