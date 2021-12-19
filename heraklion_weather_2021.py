import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = "the_csv_file_format\data\heraklion_weather_2021.csv"

# import the dataset
with open(filename) as f:
    # read the dataset
    reader = csv.reader(f)
    # read the 1st row
    header_row = next(reader)
    # print the 1st row
    print(header_row)

    # print each col with its index
    for index, col in enumerate(header_row):
        print(index, col)

    # create empty lists to later store the values
    tmax, tmin, dates = [], [], []

    for row in reader:
        try:
            # access each value of the cols of interest
            date = datetime.strptime(row[2], "%Y-%m-%d")
            temp_min = int(row[7])
            temp_max = int(row[6])
        except ValueError:
            # print the row where missing data are
            print(f"Missing data in {date}")
        else:
            # append each value on the respective list
            tmin.append(temp_min)
            tmax.append(temp_max)
            dates.append(date)

# plot high and low temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates, tmin, c='blue', alpha=0.5)
ax.plot(dates, tmax, c='red', alpha=0.5)
ax.fill_between(dates, tmin, tmax, facecolor='blue', alpha=0.1)

# format the plot
ax.set_title("High and Low Daily Temperatures in Heraklion, GR - 2021",
 fontsize=24)
ax.set_xlabel("Date", fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()

plt.show()
