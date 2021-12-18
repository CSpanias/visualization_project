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
    highs, dates = [], []
    # starts from the 2nd row as it has already read the 1st above!
    for row in reader:
        # convert string to integer
        high = int(row[5])
        # convert object to datetime object
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        highs.append(high)
        dates.append(current_date)

print(highs)
print(dates)



# plot the hight temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# format plot
ax.set_title("Daily high temperatures - 2018", fontsize=24)
ax.set_xlabel("", fontsize=16)
# prevents label overlapping
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
