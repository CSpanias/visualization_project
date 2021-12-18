import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = r"C:\Users\10inm\Documents\GitHub\visualization_project\the_csv_file_format\data\death_valley_2018_simple.csv"
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
        # convert object to datetime object
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            # convert string to integer
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
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
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel("", fontsize=16)
# prevents label overlapping
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
