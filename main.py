# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager
import asyncio

flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()

# print(sheet_data)


if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:

        row["iataCode"] = flight_search.get_destination_code(city_name=row["city"])["locations"][0]["code"]

    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

ORIGIN_CITY_IATA = "DUS"
tomorrow = datetime.now() + timedelta(days=30)
six_month_from_today = datetime.now() + timedelta(days=(4 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight:
        if flight.price < destination["lowestPrice"]:
            google_url = f'https://www.google.com/travel/flights?q=Flights%20to%20{flight.destination_airport}%20from%20' \
                         f'{flight.origin_airport}%20on%20{flight.out_date}%20through%20{flight.return_date}'

            asyncio.run(notification_manager.send_telegram(
                message=f"Low price alert! Only €{flight.price}\n\n"
                        f"From: {flight.origin_city}-{flight.origin_airport}\n"
                        f"To: {flight.destination_city}-{flight.destination_airport} \n"
                        f"Dates: from {flight.out_date} to {flight.return_date}."
                        f"\n Google Flights URL: {google_url}"))







