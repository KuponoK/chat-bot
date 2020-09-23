from random import choice
def get_weather_bot_response(user_response):
    bot_response_sunny = ["dont forget your shades!", "get your sunscreen!"]
    bot_response_rainy = ["bring a coat!", "dont forget an umbrella"]
    bot_response_snowy = [
        "check the news if you got school or work!", "stay warm!"]
    bot_response_foggy = [
        "take some cool instagram photos", "stay cautious on the roads"]
    bot_response_smokey = ["bring facemask", "check local air quality"]
    if user_response == "sunny":
        return choice(bot_response_sunny)
    elif user_response == "rainy":
        return choice(bot_response_rainy)
    elif user_response == "snowy":
        return choice(bot_response_snowy)
    elif user_response == "foggy":
        return choice(bot_response_foggy)
    elif user_response == "smokey":
        return choice(bot_response_smokey)
    else:
        return "I don't recognize that weather pattern"
print("Welcome to the weather bot")
bot_response = "Please enter your current weather "
user_response = ""
while True:
    user_response = input(bot_response)
    if user_response == "done":
        break
    bot_response = get_weather_bot_response(user_response)