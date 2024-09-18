"""Practicing with ELIF"""


def get_weather_report() -> str:

    weather: str = str((input("What is the weather?")))
    if weather == "rainy" or weather == "cold":
        print("bring a jacket!")
    elif weather == "hot":
        print("keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()
