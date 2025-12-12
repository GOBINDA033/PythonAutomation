#In this program I going to do some match case statement
""" SmartHome Controller Device"""
device=input("Enter the device you want to control")
match device:
    case "Light":
        print("Trun on light")
    case "fan":
        print("Turn on Fan")
    case "AC":
        print("Turn on AC")

    case "WaterMotor":
        print("Turn on the water Motor")
    case _:
        print("Device not found")


    