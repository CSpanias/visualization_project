import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename_death_valley = r"C:\Users\10inm\Documents\GitHub\visualization_project\the_csv_file_format\data\death_valley_2018_simple.csv"
filename_sitka = r"C:\Users\10inm\Documents\GitHub\visualization_project\the_csv_file_format\data\sitka_weather_2018_simple.csv"

with open(filename_death_valley) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:

        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])

        except ValueError:
            print(f"Missing data in {current_date}")

        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# plot death valley temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, lows, highs, facecolor='blue', alpha=0.1)

# format plot
ax.set_title("Daily High and Low Temperature\nDeath Valley - 2018", fontsize=20)
ax.set_xlabel("Date", fontsize=16)
# prevents label overlapping
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 130)

plt.show()

with open(filename_sitka) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:

        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])

        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# plot Sitka temps
plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates, lows, c='blue', alpha=0.5)
ax.plot(dates, highs, c='red', alpha=0.5)
ax.fill_between(dates, lows, highs, alpha=0.1, facecolor='blue')

# format plot
ax.set_title("Daily High and Low Temperature\nSitka - 2018", fontsize=20)
ax.set_xlabel("Date", fontsize=16)
# prevents label overlapping
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 130)

plt.show()
