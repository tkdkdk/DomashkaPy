import datetime as dt
from zoneinfo import ZoneInfo, available_timezones

NAIVE_DT = dt.datetime(2000, 1, 1, 10)
for tz in available_timezones():
    print(tz)

utc_dt = NAIVE_DT.replace(tzinfo=dt.timezone.utc)

sydney_tz = ZoneInfo("Australia/Sydney")
sydney_dt = utc_dt.astimezone(sydney_tz)

la_tz = ZoneInfo("America/Los_Angeles")
la_dt = utc_dt.astimezone(la_tz)

assert utc_dt.isoformat() == "2000-01-01T10:00:00+00:00"
assert sydney_dt.isoformat() == "2000-01-01T21:00:00+11:00"
assert la_dt.isoformat() == "2000-01-01T02:00:00-08:00"

print("All good!")