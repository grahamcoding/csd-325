# Daniel Graham
# Date 6/14/25
# Week 4/Module 4.2 Assignment: Temperature Graphing


import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
#import lows as well
dates, highs, lows = [], [], []
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and temperatures from this file.
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {row[2]}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Menu loop
while True:
    print("\nWelcome to the Sitka Weather Visualizer")
    print("By Daniel Graham. Week 4/Module 4.2")
    print("\nChoose an option:")
    print("1 - View High Temperatures")
    print("2 - View Low Temperatures")
    print("3 - Exit")

    choice = input("Enter your choice (1/2/3): ")

#High Temperature Graph
    if choice == '1':
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily High Temperatures - 2018", fontsize=20)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

#Low Temperature Graph
    elif choice == '2':
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        plt.title("Daily Low Temperatures - 2018", fontsize=20)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

#Exit option
    elif choice == '3':
        print("Thanks for exploring the Sitka weather! Goodbye.")
        break

#Invalid Input
    else:
        print("Invalid input. Please enter 1, 2, or 3.")