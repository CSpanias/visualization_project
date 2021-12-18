import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = r"C:\Users\10inm\Documents\GitHub\visualization_project\the_csv_file_format\data\sitka_weather_2018_simple.csv"
# assign the file object to f
with open(filename) as f:
    reader = csv.reader(f)
    # returns the next line in the filename (in this case the headers)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # get high temperatures and dates from this file
    highs, lows, dates = [], [], []
    # starts from the 2nd row as it has already read the 1st above!
    for row in reader:
        # convert string to integer
        high = int(row[5])
        low = int(row[6])
        # convert object to datetime object
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        highs.append(high)
        lows.append(low)
        dates.append(current_date)

# plot the hight temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
# alpha controls transparency, 0 = 100% transparent / 1 = 100% opaque
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# format plot
ax.set_title("Daily high and low temperatures - 2018", fontsize=24)
ax.set_xlabel("", fontsize=16)
# prevents label overlapping
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
