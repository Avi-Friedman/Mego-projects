#the function get object that contians minuts and hours and will back amount time have until mid night
class Clock:

    def __init__(self, hour, min):
        self.hour = hour
        self.min = min

def get_interval(time):
    return(24 - time.hour) * 60 + time.min

flight_1 = Clock(8, 45)
flight_2 = Clock(10, 32)

def earlier_flight_time(flight_1, flight_2):
    if get_interval(flight_1) > get_interval(flight_2):
        print(f"flight_1 is earlier")
    else:
        print(f"flight_2 is earlier")

earlier_flight_time(flight_1,flight_2)