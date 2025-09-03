import glob
import csv

# 1. Load all CSV files
files = glob.glob("assignment_files/temperatures/*.csv")

# Dictionary: station - list of all temps
station_data = {}

#Creating a list for all the temperature values for each season to belong
summer = []
autumn = []
winter = []
spring = []

for fname in files:
    with open(fname, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header row
        for row in reader:
            station = row[0].strip()
            temps = [t for t in row[4:] if t]  # monthly temps, ignore blanks
            temps = [float(t) for t in temps if t.lower() != "nan"]  # skip NaN

            if station not in station_data:
                station_data[station] = []

            station_data[station].extend(temps)

            summer.extend([row[4], row[5], row[15]])  #looping through so that the values in the index positions of the months corresponding to each season are added
            autumn.extend([row[6], row[7], row[8]])
            winter.extend([row[9], row[10], row[11]])
            spring.extend([row[12], row[13], row[14]])
      
# Question 1: Find the average temperature for all seasons across all years

season_temps = [summer, autumn, winter, spring]      #storing all the temperatures in a nested list
season_averages = []       #creating a list to store values for each season's average
for i in range(4):
    sum = 0
    for j in range(6270):
        sum = sum + float(season_temps[i][j])
        average = sum / 6270
    season_averages.append(average)
print(season_averages)
summer_average = season_averages[0]
autumn_average = season_averages[1]
winter_average = season_averages[2]
spring_average = season_averages[3]

#Save results to file
with open("assignment_files/average_temp.txt", "w") as out:
    out.write("Summer:" + summer_average + "\n")
print("Saved results to assignment_files/average_temp.txt")





"""
# 2. Calculate range (max - min) for each station
station_ranges = {}
for station, vals in station_data.items():
    if vals:  # make sure station has some data
        mx = max(vals)
        mn = min(vals)
        rg = mx - mn
        station_ranges[station] = (rg, mx, mn)

# 3. Find the station(s) with the largest range
largest_range = -1
winners = []
for st, (rg, mx, mn) in station_ranges.items():
    if rg > largest_range:
        largest_range = rg
        winners = [(st, rg, mx, mn)]
    elif abs(rg - largest_range) < 1e-9:  # tie
        winners.append((st, rg, mx, mn))

# 4. Save results to file
with open("assignment_files/largest_temp_range_station.txt", "w") as out:
    for st, rg, mx, mn in winners:
        out.write(f"{st}: Range {rg:.1f}°C (Max: {mx:.1f}°C, Min: {mn:.1f}°C)\n")

print("Saved results to assignment_files/largest_temp_range_station.txt")
"""