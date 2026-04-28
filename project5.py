import pandas as pd
import os

class Flight:
    def __init__(self, flight_num, delay_time):
        self.flight_num = flight_num
        self.delay_time = delay_time

    def check_severity(self):
        if self.delay_time > 60:
            print(f" SEVERE DELAY: Flight {self.flight_num} delayed by {self.delay_time} minutes!")
        elif self.delay_time > 30:
            print(f" WARNING: Flight {self.flight_num} delayed by {self.delay_time} minutes!")
        else:
            print(f" Flight {self.flight_num} is on time.")

try:
    df = pd.read_csv("arrivals.csv")
except FileNotFoundError:
    print(" arrivals.csv file not found!")
    exit()

# fill missing values with 0
df["Minutes_Delayed"] = df["Minutes_Delayed"].fillna(0)

# convert to integer
df["Minutes_Delayed"] = df["Minutes_Delayed"].astype(int)

delayed_flights = df[df["Minutes_Delayed"] > 30]

if delayed_flights.empty:
    print(" No flights with delay greater than 30 minutes.")

else:

    worst_flight = delayed_flights.loc[delayed_flights["Minutes_Delayed"].idxmax()]


    flight = Flight(
        worst_flight["Flight_Number"],
        worst_flight["Minutes_Delayed"]
    )


    flight.check_severity()

    new_data = pd.DataFrame([{
        "Flight_Number": worst_flight["Flight_Number"],
        "Airline": worst_flight["Airline"],
        "Minutes_Delayed": worst_flight["Minutes_Delayed"]
    }])

    log_file = "severe_delays_log.csv"

    if os.path.exists(log_file):
        old_data = pd.read_csv(log_file)
        updated_data = pd.concat([old_data, new_data], ignore_index=True)
    else:
        updated_data = new_data

    updated_data.to_csv(log_file, index=False)

    print("severe_delays_log.csv file created/updated successfully!")