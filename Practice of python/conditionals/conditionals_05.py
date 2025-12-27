def transport_mode(distance):
    if distance < 3:
        return "walk"
    elif distance >= 3 and distance <= 15:
        return "Bike!"
    elif distance > 15 and distance <= 50:
        return "Car!"
    elif distance > 50 and distance <= 300:
        return "Train!"
    else:
        return "Plane!"
    
def main():
    distance = float(input("Enter the distance to travel in kilometers: "))
    print(f"For a distance of {distance} km, you should use : {transport_mode(distance)}")

if __name__ == "__main__":
    main()
