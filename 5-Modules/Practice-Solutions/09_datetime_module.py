import datetime

today = datetime.date.today()
print(f"Today's date: {today}")

future_date = today + datetime.timedelta(days=100)
print(f"Date 100 days from today: {future_date}")

given_date = datetime.date(2022, 1, 1)
print(f"Day of the week for 2022-01-01: {given_date.strftime('%A')}")
