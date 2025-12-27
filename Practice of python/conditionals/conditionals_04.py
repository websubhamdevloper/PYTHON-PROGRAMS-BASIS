def weather_report(weather):
    if weather == "sunny":
        return "Go for a walk!"
    elif weather == "rainy":
        return "Read Books indoors!"
    elif weather == "snowy":
        return "Build a a snowman!"
    elif weather == "foggy":
        return "Better be at home!"
    else:
        return "Be cautious while going out!"

def main():
    weather = input("Enter the weather condition (sunny, rainy, snowy, foggy) : ").lower()
    print(weather_report(weather))

if __name__ == "__main__":
    main()

