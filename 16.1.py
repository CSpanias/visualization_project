import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = r"C:\Users\10inm\Documents\GitHub\visualization_project\the_csv_file_format\data\sitka_weather_2018_simple.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get dates and rainfall amounts from this file.
    date, prcp = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            rain = float(row[3])
        except ValueError:
            print(f"Missing value for {current_date}")
        else:
            prcp.append(rain)
            date.append(current_date)

# generate a plot
plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(date, prcp, c='blue')

# format plot
ax.set_title("Sitka Rainfall - 2018", fontsize=20)
ax.set_xlabel("Date", fontsize=16)
# prevents label overlapping
fig.autofmt_xdate()
ax.set_ylabel("Prepicitation", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
